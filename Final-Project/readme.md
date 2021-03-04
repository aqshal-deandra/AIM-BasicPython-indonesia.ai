Nama : Aqshal Deandra Vandaru

Kelompok : B

## Final Project AIM Basic Python

**Tujuan** : Membuat sebuah program python yang dapat mengirimkan email kepada beberapa penerima.
Daftar email penerima disimpan dalam file format .txt

## Hasil Penugasan

Program menjalankan kode yang dapat dilihat di [final_project](final_project.py) dan akan mengirim 
email beserta attachment kepada penerima yang telah dimasukan pada [daftar email](attachment)

Pertama-tama program akan meminta memasukkan password akun email pengirim seperti gambar dibawah.

![input_password](https://user-images.githubusercontent.com/78999297/109990834-57d4b680-7d3c-11eb-9745-95c2c8732938.png)


Karena telah menggunakan library *getpass* sebelumnya maka ketika kita mengetik password, password tidak akan terlihat.

Selanjutnya, program akan me-looping sebanyak email penerima yang ada pada [daftar_email]

![proses_pengiriman](https://user-images.githubusercontent.com/78999297/109992193-9c148680-7d3d-11eb-8f39-d8d7f0bc565a.png)


Setelah program selesai dijalankan maka kita bisa langsung mengecek apakah email sudah masuk atau belum

![email_terkirim2](https://user-images.githubusercontent.com/78999297/109996270-a3d62a00-7d41-11eb-899d-b34ed764edc3.png)


Email serta attachment telah berhasil terkirim. Penerima ada dua orang sesuai jumlah email yang ada pada [daftar_email]

Dari hasil diatas kita juga dapat mengatur nama pengirim yang bisa dilihat dari potongan kode


```python
sender_email = "wheremybrainp@gmail.com"
sender_name = "Python-Dean"
```

Dan juga agar email lebih fleksibel pada subject email kita bisa menyesuaikan panggilan 
sapaan yang didapat dari nama sebelum tanda @ pada email penerima

```python
msg['Subject'] = 'Hello, ' + receiver_name + '. This is my AIM Basic Python Final Project'
```

![body_email](https://user-images.githubusercontent.com/78999297/109995259-b865f280-7d40-11eb-9f54-040526fa233e.png)


Itu merupakan tampilan full body email dengan bantuan format html.


##Referensi
- Kode python smtplib : https://www.youtube.com/watch?v=m9ojKEBYCvQ&list=PLySH_9QSmELPMujUA-oaGZYUs_igjaNWf&index=4&t=262s
- Read file : https://www.youtube.com/watch?v=_nCccpFeAN4&t=350s
- Body Email : https://beefree.io/
- Hide Password : https://www.youtube.com/watch?v=OZT7Wxru68Q&t=176s

