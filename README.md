# Deteksi Bentuk Dasar Geometri Berdasarkan Knowledge-Based System

Disusun oleh:

- Andrian Cedric 13517065
- Ferdy Santoso 13517116
- Vincent Budianto 13517131
- Jan Meyer Saragih 13517137

## Tahapan Pembangunan Aplikasi

Aplikasi ini dibangun dengan menggabungkan 3 jenis proses utama yaitu:

- Pendeteksian gambar
- Rule processing
- GUI

### Deteksi Gambar

Deteksi gambar menggunakan library bahasa Python bernama OpenCV. OpenCV merupakan library yang dapat mendeteksi pola yang terbentuk di dalam berkas dengan tipe berkas gambar (.jpg, .png, dan kawan-kawannya). Dengan memanfaatkan contour, OpenCV mampu mendeteksi perubahan warna yang terdapat pada gambar dan menentukan titik-titik sudut yang dimiliki oleh gambar.

OpenCV contour mengembalikan titik-titik sudut yang dikelompokkan per  bentuk. Namun, dia juga mengembalikan bentuk container dari gambar tersebut.  Maka dari itu, perlu dilakukan filter image terlebih dahulu, yaitu bentuk yang dideteksi bukanlah bentuk yang berada pada absis atau ordinat 0.

Setelah mendapatkan titik-titik sudut, maka dilakukan perhitungan untuk mendapatkan panjang garis antar 2 titik tersebut, sudut yang dimiliki oleh titik tersebut, serta gradien pada setiap garis. Setelah itu, data ini di-pass ke dalam modul pemrosesan dengan KBS

### Rule processing

Rule processing memanfaatkan library bahasa Python bernama ClipsPy. Selain itu, digunakan juga sebuah file CLIPS yang berfungsi sebagai mesin knowledge based system (KBS).

Setelah mendapatkan daftar garis, sudut, gradien, dan jumlah titik sudut dari pendeteksian gambar, diambil bentuk pertama yang terdeteksi. Setiap informasi mengenai gambar tersebut di-assert ke dalam environment CLIPS yang dibuat oleh ClipsPy. Setelah itu CLIPS dijalankan dan result dapat dilihat dan dikirimkan ke GUI

### GUI

Graphical User Interface merupakan tempat bagi user untuk memasukkan gambar yang dibutuhkan oleh aplikasi. Selain itu, user juga dapat mengeksekusi gambar tersebut agar dapat dijalankan oleh proses deteksi gambar dan rule processing. Hasil dari kedua proses tersebut didapatkan oleh GUI untuk ditampilkan kembali ke user.

## Repository yang Berisi Dokumentasi Lengkap

Link ke repository : https://github.com/vincentbudianto/Shaper

## User Manual secara Lengkap

Berikut ini merupakan tampilan GUI kami :

![Mockup](https://i.imgur.com/hj9vR8X.png)

Bagian-bagian GUI kami terdiri dari :

- Source Image

    Tempat untuk menampilkan gambar yang dipilih oleh pengguna.

- Detection Image

    Tempat untuk menampilkan bentuk yang ingin dideteksi oleh pengguna.

- Open Image

    Tombol untuk membuka window pemilihan gambar dari komputer menggunakan file browser.

- Open Rule Editor

    Tombol untuk membuka text editor file yang berisi rules yang telah kami buat.

- Show Rules

    Tombol untuk menampilkan seluruh rules yang dimiliki oleh program rule processing kami (CLIPS).

- Show Facts

    Tombol untuk menampilkan seluruh fakta yang dimiliki oleh program rule processing kami (CLIPS).

- Pilihan Bentuk

    Berisi checkbox, digunakan untuk menentukkan bentuk apa yang ingin dideteksi oleh pengguna.

- Detection Result

    Tempat untuk menampilkan hasil deteksi mesin atas gambar yang dipilih oleh pengguna. Hasil dapat berupa true atau false.

- Matched Facts

    Tempat untuk menampilkan fakta-fakta yang didapatkan/digunakan oleh mesin.

- Hit Rules

    Tempat untuk menampilkan rules yang digunakan oleh mesin.

Berikut ini adalah langkah-langkah yang dapat dilakukan oleh pengguna untuk menggunakan program kami :

1. Install Kivy pada komputer pengecek

    Setelah install Kivy, letakkan Kivy.md di folder Python pada komputer Anda.

2. Buka File Python

    python shaper.py

3. Masukkan gambar

    Pengguna dapat memasukkan gambar dengan menekan tombol “Open Image”. Perlu diperhatikan bahwa gambar yang dimasukkan adalah gambar dengan format PNG.

4. Pilih shape

    Lakukan pemilihan bentuk melalui menu “Pilihan Bentuk” di bagian kanan.

5. Tunggu hasil program.

    Tunggu hasil program saat sedang melakukan deteksi bentuk pada gambar anda.

6. Hasil ditampilkan

    Setelah selesai, hasil akan ditampilkan di layar. Hasil inferensi akan ditampilkan pada bagian “Detection Result”, hasil fakta yang digunakkan/didapatkan mesin pada bagian “Matched Facts”, dan Hasil rules yang digunakan pada bagian “Hit Rules”.

## Proses Updating dan Inferencing atas Fakta yang Terlibat

Fakta yang terlibat di-update dengan menggunakan forward chaining dengan CRS default dari CLIPS yaitu depth first (fact recency). Tentunya rule CRS ini masih mempunyai prioritas lebih rendah dari rule CRS refactoriness, sehingga daftar rulenya adalah refactoriness > fact recency.

Yang dilakukan oleh mesin inferensi adalah mendata semua fakta yang ada sebelum memulai proses inferensi. Setelah itu, memutuskan apakah terdapat rules yang dapat dimasukkan ke dalam working memory atau harus dikeluarkan dari working memory. Keputusan ini didapatkan dari fakta-fakta yang dimiliki oleh mesin inferensi sekarang.

Pada CLIPS, cara pengecekan bahwa sebuah rule dapat dimasukkan ke dalam working memory hanyalah dengan menggunakan sisi kiri dari rules tersebut. Jika sisi kiri rules tersebut terpenuhi oleh semua fact yang dikumpulkan sekarang, maka rules tersebut layak dimasukkan ke dalam working memory.

Setelah mendapatkan rule yang dapat dieksekusi, dipilih satu rule menggunakan CRS (Conflict Resolution Strategy), yaitu refactoriness > fact recency. Eksekusi rule tersebut dan setelah dieksekusi, fakta yang terdapat pada sisi kanan dari rule tersebut akan dimasukkan ke atau dikeluarkan dari daftar fakta yang ada.

Dengan demikian, proses updating pun dimulai dan mesin akan dapat menentukan rules-rules mana yang mampu dimasukkan ke dalam working memory pada proses yang berikutnya. Hal ini dilakukan terus-menerus hingga tidak ada rule yang dapat dimasukkan ke dalam working memory.
