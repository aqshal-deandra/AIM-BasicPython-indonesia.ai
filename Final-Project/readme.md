Nama : Aqshal Deandra Vandaru

Kelompok : B

## Final Project AIM Basic Python

**Tujuan** : Membuat sebuah program python yang dapat mengirimkan email kepada beberapa penerima.
Daftar email penerima disimpan dalam file format .txt

## Hasil Penugasan

Program menjalankan kode yang dapat dilihat di [final_project](final_project.py) dan akan mengirim 
email kepada penerima yang telah dimasukan pada [daftar email]

Pertama-tama program akan meminta memasukkan password akun email pengirim seperti gambar dibawah.

![input_password](https://user-images.githubusercontent.com/78999297/109990834-57d4b680-7d3c-11eb-9745-95c2c8732938.png)


Karena telah menggunakan library *getpass* sebelumnya maka ketika kita mengetik password, password tidak akan terlihat.

Selanjutnya, program akan me-looping sebanyak email penerima yang ada pada [daftar_email]

![proses_pengiriman](https://user-images.githubusercontent.com/78999297/109992193-9c148680-7d3d-11eb-8f39-d8d7f0bc565a.png)


Setelah program selesai dijalankan maka kita bisa langsung mengecek apakah email sudah masuk atau belum

![email_terkirim](https://user-images.githubusercontent.com/78999297/109993076-7fc51980-7d3e-11eb-9346-92423a81d294.png)


Email telah berhasil terkirim

Dari hasil diatas kita juga dapat mengatur nama pengirim yang bisa dilihat dari potongan kode

```python
sender_email = "wheremybrainp@gmail.com"
sender_name = "Python-Dean"
```

