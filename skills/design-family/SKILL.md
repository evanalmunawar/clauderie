---
name: design-family
description: Bikin halaman/produk baru yang terasa "sekeluarga" dengan desain induk yang sudah ada — DNA (warna, font, spacing, navbar, footer) tetap sama, tapi section/layout isi disesuaikan ulang untuk kebutuhan produk baru. Dipakai saat user kirim desain/token lama dan minta turunan produk baru darinya.
---

# Design Family

Skill ini untuk membuat desain baru yang **bukan desain lepas dari nol**, tapi turunan dari desain induk yang sudah ada — mirip tapi tidak 100% identik, dan boleh punya elemen yang sama sekali tidak ada di induknya kalau produk barunya memang butuh itu.

## Kapan skill ini dipakai

Trigger: user mengirim file (zip, repo, satu file HTML, atau `token.css`/variabel desain) dan bilang sesuatu seperti "mau bikin produk X dari desain ini" / "turunan dari landing ini". Bukan untuk desain pertama dari nol (itu `catchy-frontend-design`) dan bukan untuk revisi satu elemen (itu `design-revision-flow`).

## Yang WAJIB sama (DNA)

Ambil dari file yang dikirim user, jangan diubah kecuali diminta:
- Token warna (termasuk dark/light mode kalau ada)
- Font family + font-weight yang dipakai
- Spacing/padding scale
- Ukuran font (type scale)
- Border-radius yang jadi kebiasaan desain itu (misal selalu `4px` atau selalu pill)
- Navbar dan footer — strukturnya tetap sama; isi link/brand name boleh menyesuaikan produk baru

## Yang BOLEH beda (konten adaptif)

- Layout section di badan halaman — disesuaikan sepenuhnya dengan kebutuhan produk baru
- Section/komponen yang sama sekali tidak ada di induk, kalau produk baru memang butuh (misal: induk cuma hero teks+gradasi, tapi produk baru adalah link-bio tool yang butuh mockup produk/preview interaktif — mockup ini baru, tidak ada acuannya di induk, dan itu wajar)
- Copy/konten tentu saja berbeda sesuai produk

Saat bikin elemen baru yang tidak ada di induk, tetap gunakan DNA (warna/font/spacing/radius) supaya terasa buatan keluarga yang sama meski bentuknya baru.

## Alur kerja

1. **Baca file yang dikirim user.** Kalau berupa HTML/repo lengkap, ekstrak DNA langsung dari situ (warna dari CSS variables atau nilai yang berulang, font dari `font-family`, spacing dari pola padding/margin yang konsisten). Kalau hanya `token.css` atau sejenisnya, DNA warna/font/spacing sudah jelas, tapi struktur komponen (navbar/footer/section pattern) tidak diketahui.

2. **Kalau info DNA tidak lengkap** (contoh: user cuma kirim token.css, tidak ada contoh navbar/footer/komponen), **jangan menebak sendiri**. Tawarkan ke user secara eksplisit:
   - "Saya cuma punya token warna/font dari file ini, belum ada contoh navbar/footer-nya. Mau saya kreasikan bagian itu bebas (tetap pakai token warna/fontnya), atau ada file lain/link repo yang bisa dikirim biar lebih konsisten?"

   Jangan lanjut desain dengan asumsi diam-diam soal struktur yang tidak diketahui.

3. **Pahami kebutuhan produk baru dari user** — section apa saja yang dibutuhkan, elemen baru apa yang tidak ada di induk (contoh klasik: produk link-bio butuh mockup/preview, landing page biasa tidak).

4. **Desain section/layout baru** mengikuti DNA yang sudah diambil, pakai prinsip dari `catchy-frontend-design` untuk bagian yang memang baru (tidak ada presedennya di induk).

5. **Hasil akhir dicek**: apakah terlihat seperti dari keluarga yang sama kalau diletakkan berdampingan dengan induknya? Warna/font/spacing harus langsung dikenali sama; tapi layout dan section boleh total berbeda.

## Yang harus dihindari

- Jangan copy-paste struktur section induk mentah-mentah ke produk baru kalau kebutuhannya beda — itu bukan "sekeluarga", itu duplikat yang dipaksa.
- Jangan mengubah token warna/font/spacing induk tanpa diminta eksplisit oleh user.
- Jangan menebak struktur navbar/footer/komponen yang tidak ada di file yang dikirim — tawarkan pilihan ke user dulu (lihat langkah 2).
- Jangan bikin elemen baru (seperti mockup) menyimpang dari DNA warna/font hanya karena elemennya baru.
