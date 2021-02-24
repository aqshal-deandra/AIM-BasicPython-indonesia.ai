# Tugas 2 - Aqshal Deandra Vandaru

# Membuat list dictionary daftar kontak
daftar_kontak = []

# Method melihat daftar kontak
def lihat_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("---**---")
        print(f"Nama : {kontak['nama']}")
        print(f"No Telepon : {kontak['telepon']}")

# Method menambahkan kontak
def tambah_kontak():
    nama = input("Nama : ")
    telepon = input("No Telepon : ")
    kontak = {
        "nama": nama,
        "telepon": telepon
    }
    return kontak


print("Selamat Datang!")

while True:
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    # Apabila input 3 maka program berakhir
    if menu == "3":
        break
    # input 1 untuk melihat daftar kontak
    elif menu == "1":
        lihat_kontak(daftar_kontak)
    # input 2 untuk menambah kontak
    elif menu == "2":
        kontak = tambah_kontak()
        daftar_kontak.append(kontak)
        print("Kontak berhasil ditambahkan.")
    # apabila input selain angka di menu
    else:
        print("Menu tidak tersedia")

print("Program selesai, sampai jumpa!")
