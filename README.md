# clauderie

Kumpulan **skill** untuk Claude — tempat nyimpen dan ngembangin skill lintas topik, bukan cuma satu arah. Dimulai dari skill-skill desain frontend: bikin desain baru yang catchy/tidak generik, revisi elemen spesifik lewat varian interaktif, dan bikin produk turunan yang "sekeluarga" dengan desain induk yang sudah ada.

Repo ini dikemas sebagai **Claude Code plugin**, jadi bisa diinstall satu baris lewat marketplace lokal — tapi tiap skill juga bisa dipakai lepas (copy folder-nya saja) kalau tidak mau pakai sistem plugin.

Repo ini akan terus bertambah skill-nya seiring waktu, nggak cuma soal desain — tinggal tambah folder baru di `skills/`.

## Isi

| Skill | Dipakai kapan |
|---|---|
| [`catchy-frontend-design`](skills/catchy-frontend-design/SKILL.md) | Pelengkap skill `frontend-design` bawaan Claude — aturan konkret soal spacing, navbar, anti-card-generik, dan background kreatif supaya hasil desain tidak terasa template SaaS pada umumnya. |
| [`design-revision-flow`](skills/design-revision-flow/SKILL.md) | Saat user komplain satu elemen spesifik di desain yang sudah ada (misal "CTA jangan card") — menawarkan beberapa varian ringan lewat satu artifact dengan toggle, bukan langsung redesain total. |
| [`design-family`](skills/design-family/SKILL.md) | Saat user mau bikin produk/halaman baru yang jadi "turunan" dari desain yang sudah ada — DNA (warna, font, spacing, navbar/footer) dipertahankan, tapi layout dan section isi boleh disesuaikan total untuk kebutuhan produk baru. |

Ketiga skill ini saling melengkapi dan dirancang untuk dipakai bersama skill `frontend-design` bawaan Claude (bukan pengganti).

---

## Cara install

### A. Di Claude Code (sebagai plugin)

**Opsi 1 — lewat marketplace (repo ini sendiri jadi marketplace-nya):**

```bash
/plugin marketplace add evanalmunawar/clauderie
/plugin install clauderie@clauderie-marketplace
```

**Opsi 2 — langsung dari folder lokal (tanpa publish/tanpa git), cocok untuk development:**

```bash
claude --plugin-dir /path/ke/repo/ini
```

**Opsi 3 — clone dulu baru add sebagai marketplace lokal:**

```bash
git clone https://github.com/evanalmunawar/clauderie.git
cd clauderie
claude
# di dalam sesi Claude Code:
/plugin marketplace add .
/plugin install clauderie@clauderie-marketplace
```

Setelah terinstall, skill-skill di dalamnya otomatis aktif sesuai konteks (Claude akan pakai sendiri saat relevan — tidak perlu dipanggil manual), dan juga bisa dijalankan sebagai command langsung, misal `/clauderie:catchy-frontend-design`.

Cek status plugin kapan saja dengan `/plugin`.

### B. Di claude.ai (chat biasa, bukan Claude Code)

Sistem plugin di atas khusus Claude Code. Di claude.ai, upload isi salah satu folder `skills/<nama-skill>/` (minimal file `SKILL.md`-nya) sebagai skill custom lewat menu skill di pengaturan, atau cukup lampirkan file `SKILL.md`-nya ke percakapan dan minta Claude membacanya sebagai panduan sebelum mengerjakan desain.

---

## Struktur repo

```
.
├── .claude-plugin/
│   ├── plugin.json        # manifest plugin
│   └── marketplace.json   # katalog, supaya repo ini bisa langsung di-add sebagai marketplace
├── skills/
│   ├── catchy-frontend-design/
│   │   └── SKILL.md
│   ├── design-revision-flow/
│   │   └── SKILL.md
│   └── design-family/
│       └── SKILL.md
└── README.md
```

## Menambah skill baru

1. Buat folder baru di `skills/<nama-skill-kebab-case>/`
2. Isi dengan `SKILL.md` (format: frontmatter `name` + `description`, lalu isi panduan)
3. Tidak perlu daftarkan manual di `plugin.json` — field `"skills": "./skills"` sudah membuat Claude Code auto-discover semua subfolder di dalamnya
4. Update tabel "Isi" di README ini

## Validasi plugin (opsional, sebelum publish)

```bash
claude plugin validate .
```
