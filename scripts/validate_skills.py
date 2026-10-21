#!/usr/bin/env python3
"""
Validasi struktur plugin clauderie:
- .claude-plugin/plugin.json dan marketplace.json harus JSON valid dengan field wajib
- Setiap skills/<nama>/SKILL.md harus:
  - ada (bukan folder kosong)
  - punya frontmatter YAML (--- ... ---) di awal file
  - frontmatter punya field "name" dan "description"
  - "name" di frontmatter = nama foldernya (kebab-case, konsisten)
  - "description" tidak kosong dan tidak kepanjangan tanpa batas (biar nggak nyampah context)
  - folder pakai kebab-case (huruf kecil, angka, strip)

Exit code 0 kalau semua valid, 1 kalau ada error (ini yang bikin GitHub Actions merah).
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_JSON = REPO_ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = REPO_ROOT / "skills"

KEBAB_CASE_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_DESCRIPTION_LEN = 1024  # longgar, cuma biar nggak ada yang lupa isi paragraf penuh

errors = []
warnings = []


def fail(msg: str):
    errors.append(msg)


def warn(msg: str):
    warnings.append(msg)


def check_json_file(path: Path, required_fields: list[str]):
    if not path.exists():
        fail(f"File wajib tidak ditemukan: {path.relative_to(REPO_ROOT)}")
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"{path.relative_to(REPO_ROOT)}: JSON tidak valid ({e})")
        return None
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            fail(f"{path.relative_to(REPO_ROOT)}: field '{field}' wajib ada dan tidak boleh kosong")
    return data


def parse_frontmatter(text: str, skill_path: Path):
    """Ambil blok frontmatter YAML sederhana di antara '---' di awal file."""
    if not text.lstrip().startswith("---"):
        fail(f"{skill_path}: SKILL.md harus mulai dengan frontmatter '---'")
        return None

    lines = text.splitlines()
    # cari '---' pembuka (baris pertama non-kosong) dan '---' penutup
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            start_idx = i
            break
    if start_idx is None:
        fail(f"{skill_path}: tidak menemukan baris '---' pembuka frontmatter")
        return None

    end_idx = None
    for i in range(start_idx + 1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        fail(f"{skill_path}: frontmatter tidak ditutup dengan '---'")
        return None

    frontmatter_lines = lines[start_idx + 1:end_idx]
    data = {}
    current_key = None
    for raw_line in frontmatter_lines:
        if not raw_line.strip():
            continue
        if raw_line.startswith((" ", "\t")) and current_key:
            # lanjutan value multi-baris sederhana, gabungkan
            data[current_key] += " " + raw_line.strip()
            continue
        if ":" not in raw_line:
            fail(f"{skill_path}: baris frontmatter tidak valid (bukan 'key: value'): {raw_line!r}")
            continue
        key, _, value = raw_line.partition(":")
        key = key.strip()
        value = value.strip()
        data[key] = value
        current_key = key

    return data


def check_skill(skill_dir: Path):
    folder_name = skill_dir.name

    if not KEBAB_CASE_RE.match(folder_name):
        fail(
            f"skills/{folder_name}: nama folder harus kebab-case "
            f"(huruf kecil, angka, strip saja) — ditemukan '{folder_name}'"
        )

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        fail(f"skills/{folder_name}: SKILL.md tidak ditemukan")
        return

    text = skill_md.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"skills/{folder_name}/SKILL.md: file kosong")
        return

    rel = f"skills/{folder_name}/SKILL.md"
    frontmatter = parse_frontmatter(text, rel)
    if frontmatter is None:
        return

    name = frontmatter.get("name", "").strip()
    description = frontmatter.get("description", "").strip()

    if not name:
        fail(f"{rel}: frontmatter field 'name' wajib ada dan tidak kosong")
    elif name != folder_name:
        fail(
            f"{rel}: frontmatter 'name: {name}' tidak sama dengan nama folder "
            f"'{folder_name}' — harus konsisten"
        )

    if not description:
        fail(f"{rel}: frontmatter field 'description' wajib ada dan tidak kosong")
    elif len(description) > MAX_DESCRIPTION_LEN:
        warn(
            f"{rel}: description cukup panjang ({len(description)} karakter) — "
            f"pertimbangkan dipersingkat supaya hemat context"
        )

    # body minimal harus ada isi di luar frontmatter
    body_after_frontmatter = text.split("---", 2)
    if len(body_after_frontmatter) < 3 or not body_after_frontmatter[2].strip():
        fail(f"{rel}: tidak ada isi panduan setelah frontmatter")


def main():
    print("== Validasi clauderie ==\n")

    plugin_data = check_json_file(PLUGIN_JSON, required_fields=["name", "description"])
    check_json_file(MARKETPLACE_JSON, required_fields=["name", "plugins"])

    if not SKILLS_DIR.exists():
        fail("Folder skills/ tidak ditemukan")
    else:
        skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
        if not skill_dirs:
            fail("Folder skills/ kosong — tidak ada skill untuk divalidasi")
        for skill_dir in skill_dirs:
            check_skill(skill_dir)

    if plugin_data is not None:
        declared_skills_path = plugin_data.get("skills", "")
        if declared_skills_path and declared_skills_path.strip("./") != "skills":
            warn(
                f"plugin.json field 'skills' bernilai '{declared_skills_path}', "
                f"pastikan ini memang path yang dimaksud"
            )

    print(f"Skill ditemukan: {len(list(SKILLS_DIR.glob('*/SKILL.md'))) if SKILLS_DIR.exists() else 0}\n")

    if warnings:
        print("Peringatan:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("Error:")
        for e in errors:
            print(f"  - {e}")
        print(f"\n❌ Validasi gagal: {len(errors)} error ditemukan.")
        sys.exit(1)

    print("✅ Semua skill valid.")
    sys.exit(0)


if __name__ == "__main__":
    main()
