---
name: design-revision-flow
description: Alur menangani komplain/revisi spesifik dari user terhadap satu elemen desain (misal "CTA jangan card") — tawarkan beberapa varian ringan lewat satu artifact dengan toggle/switch sebelum redesain total. Nyambung dengan skill catchy-frontend-design, dipakai saat fase revisi bukan desain awal.
---

# Design Revision Flow

Skill ini khusus untuk momen **revisi**, setelah ada desain awal dan user komplain soal bagian tertentu. Bukan untuk desain dari nol (itu urusan `catchy-frontend-design` / `frontend-design`).

## Kapan skill ini dipakai

User kasih komplain **spesifik ke satu elemen**, bukan request fitur baru. Contoh pemicu:
- "ini CTA-nya gamau card"
- "section ini kaku banget"
- "warnanya kurang pas deh"
- "navbar-nya kegedean" (lihat contoh kasus nyata yang sudah terjadi)

Bukan pemicu skill ini: request desain baru dari nol, request section baru, pertanyaan teknis (bukan soal selera visual).

## Alur

1. **Jangan langsung redesain total dari komplain pertama.** Komplain user biasanya nunjuk ke satu *aspek* (misal "jangan card"), bukan brief lengkap gaya baru.

2. **Tawarkan varian ringan dari elemen yang sama** — perubahan minimal yang masuk akal dari komplain itu. Jumlah varian **tidak dibatasi 2** — kalau ada 3-4 pendekatan yang masuk akal, semua ditawarin. Contoh untuk "CTA jangan card":
   - Outline-only (border tanpa fill)
   - Background transparan/semi-transparan
   - Text-link dengan underline animasi (tanpa border sama sekali)
   - Ghost button dengan hover-fill

   Pakai penilaian — jangan paksa bikin banyak varian kalau sebenarnya cuma 2 pendekatan yang masuk akal untuk kasus itu.

3. **Semua varian masuk ke satu artifact (HTML), dengan toggle/switch** di atas elemen yang direvisi — bukan beberapa artifact terpisah, bukan cuma deskripsi teks. User harus bisa klik dan lihat langsung, bukan membayangkan dari kata-kata. Elemen di sekitar (section lain yang tidak dikomplain) tetap sama persis seperti desain sebelumnya — supaya user fokus bandingin yang direvisi saja, bukan terganggu konteks yang ikut berubah.

4. **Kalau user pilih salah satu** → terapkan itu ke desain utama (artifact asli), selesai.

5. **Kalau user masih belum cocok dari semua varian yang ditawarkan** → ini sinyal bahwa masalahnya bukan di detail styling, tapi di pendekatan elemen itu sendiri. Redesain total bagian tersebut (boleh ganti bentuk elemen sepenuhnya, bukan cuma ganti border/background), lalu ulangi dari langkah 2 jika perlu.

## Cara bikin toggle preview

Build sebagai satu file HTML (`frontend-design`/`catchy-frontend-design` tetap berlaku untuk styling tiap varian):
- Container elemen yang direvisi diberi beberapa versi (misal beberapa `<div class="variant">` disembunyikan/ditampilkan via JS), atau satu elemen dengan class yang berubah lewat JS sesuai varian aktif.
- Toggle di atas elemen: baris kecil berisi nama tiap varian (misal pill/tab kecil: "Outline" / "Transparan" / "Text-link"), bukan dropdown tersembunyi — harus langsung kelihatan ada pilihan.
- Varian aktif ditandai jelas (misal warna aktif beda) supaya user tahu sedang lihat yang mana.
- State disimpan di JS variable biasa (bukan localStorage — lihat batasan artifact).
- Publish sebagai artifact (bukan hanya ditunjukkan di chat) supaya interaktif dan bisa diklik.

## Yang harus dihindari

- Jangan tawarkan varian dalam bentuk teks/deskripsi saja ("mau yang A atau B?") tanpa visual — ini yang secara eksplisit tidak diinginkan.
- Jangan langsung lompat ke redesain total di komplain pertama sebelum menawarkan varian ringan.
- Jangan ubah bagian lain yang tidak dikomplain saat membuat preview varian — supaya perbandingan adil dan user tidak bingung membedakan apa yang berubah.
- Jangan batasi diri ke tepat 2 varian kalau ada ide lebih yang relevan dan masuk akal.
