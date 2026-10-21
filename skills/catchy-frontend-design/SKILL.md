---
name: catchy-frontend-design
description: Panduan tambahan untuk desain frontend yang lebih hidup/immersive — proporsi spacing konkret, aturan anti-card-generik, navbar (standar vs floating), dan background kreatif (CSS/video/3D) dengan performa terjaga. Dipakai BERSAMA skill frontend-design bawaan, bukan pengganti.
---

# Catchy Frontend Design

Skill ini pelengkap `frontend-design` (skill bawaan). Baca `frontend-design` dulu untuk arah aesthetic/typography/copy. Skill ini isinya aturan yang lebih konkret dan teknis: proporsi, spacing, navbar, dan background kreatif — supaya hasilnya tidak terasa generik seperti kit SaaS pada umumnya.

## Prinsip utama

Target bukan "website yang rapi", tapi website yang terasa **hidup dan dirancang**, dengan performa tetap dijaga. Dua kesalahan yang harus dihindari:
1. Semua section pakai card membulat dengan shadow abu-abu seragam — ini default generik yang paling gampang ketahuan.
2. Background cuma warna solid/flat tanpa tekstur, gradasi, atau gerakan — terasa kosong dan template.

## Spacing & proporsi (angka pasti, bukan rasa)

Pakai skala spacing konsisten, kelipatan 4px: `4, 8, 12, 16, 24, 32, 48, 64, 96, 128`. Jangan pakai angka acak seperti `13px` atau `22px`.

- **Padding section vertikal**: minimal `clamp(4rem, 10vw, 7rem)` — section yang terlalu rapat terasa murah.
- **Padding section horizontal**: `clamp(1.5rem, 5vw, 4rem)`.
- **Line-height body**: 1.6–1.7 untuk sans-serif, 1.7–1.8 untuk serif.
- **Max-width konten teks**: 60–80 karakter per baris (lihat `frontend-design` untuk ini juga).
- **Whitespace itu elemen desain, bukan sisa ruang** — jangan isi penuh tiap section dengan konten supaya "terlihat rapi"; beri ruang kosong yang disengaja di sekitar elemen penting (terutama hero).

Type scale: pakai rasio konsisten (1.25 atau 1.333), bukan ukuran acak:
```
12 / 14 / 16 / 20 / 25 / 31 / 39 / 49 / 61px  (rasio ~1.25)
```

## Hindari "kit kartu generik"

Sebelum pakai card, tanya: apakah konten ini memang butuh dibungkus kotak terpisah (misal: perbandingan harga, produk)? Kalau tidak, pertimbangkan alternatif:
- **Grid baris dengan divider garis tipis** (`border-bottom`) + hover yang geser/highlight, bukan shadow.
- **Layout asimetris** (misal grid `1fr 1.6fr`) alih-alih kolom simetris identik.
- Kalau card memang perlu, variasikan border-radius/elevation berdasarkan hierarki — jangan satu radius dan satu shadow `rgba(0,0,0,.1)` untuk semua.

## Navbar: dua mode

**Mode standar** — dipakai kalau brief serius/korporat atau butuh banyak item nav:
- Full-width, sticky di atas.
- Tinggi wajar: padding vertikal `0.9–1.1rem` (bukan `1.5rem+` — itu kegedean dan kaku).
- Border-bottom tipis atau backdrop-blur, bukan shadow tebal.

**Mode kreasi (floating pill)** — default untuk brief yang ingin terasa modern/catchy:
- `position:fixed`, melayang dengan margin dari tepi (`top:1rem`), lebar dibatasi (`min(94%, 70rem)`), center horizontal.
- `border-radius:999px`, backdrop-blur, background semi-transparan.
- Padding lebih ringkas: `0.6–0.8rem` vertikal.
- Beri jarak tambahan ke hero di bawahnya (`padding-top` section pertama ditambah tinggi navbar) supaya tidak menabrak konten.

Pilih salah satu berdasarkan brief; jangan campur ciri keduanya (misal full-width tapi pill-shaped).

## Background kreatif (CSS / video / 3D)

Background bukan harus warna flat. Urutan dari ringan ke berat — pilih seringan mungkin yang masih sesuai brief:

1. **CSS gradient mesh + noise/grain** (termurah, selalu boleh dipakai): beberapa `radial-gradient` ditumpuk dengan opacity rendah, animasi `background-position` halus (durasi 15–20s, `ease-in-out`), ditambah noise SVG tipis (opacity ≤0.06) untuk tekstur. Selalu bungkus animasi dengan `@media (prefers-reduced-motion: reduce)`.
2. **CSS pattern/shape kompleks** (grid garis, blob SVG, mesh gradient manual) — masih ringan, cocok untuk hero sekunder atau section.
3. **Video loop** — hanya untuk hero utama, bukan tiap section. Syarat: `muted autoplay loop playsinline`, durasi pendek (≤10 detik loop), kompres agresif, `poster` image sebagai fallback, dan selalu ada fallback statis untuk `prefers-reduced-motion`.
4. **3D/WebGL (three.js, shader)** — hanya kalau brief benar-benar butuh (produk visual/teknologi, portfolio kreatif). Batasi ke satu elemen hero saja, lazy-load setelah page interactive, sediakan fallback gradient statis kalau WebGL gagal/lambat.

**Aturan performa non-negotiable**: animasi background tidak boleh bikin First Contentful Paint lambat. Gradient/noise CSS boleh langsung; video/3D harus lazy atau defer. Selalu cek `prefers-reduced-motion`.

## Checklist sebelum selesai

- [ ] Tidak semua section pakai card dengan shadow yang sama
- [ ] Navbar: mode dipilih sesuai brief, tinggi tidak berlebihan
- [ ] Hero punya background bertekstur/gerak (bukan flat polos), kecuali brief minta minimalis ekstrem
- [ ] Spacing pakai skala konsisten (4px base)
- [ ] Ada satu elemen "berani" yang jadi fokus, sisanya tenang (lihat `frontend-design`)
- [ ] Responsive sampai mobile, `prefers-reduced-motion` dihormati
- [ ] Tidak ada CSS yang tabrakan spesifisitas antar section
