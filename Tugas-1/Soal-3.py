# Aqshal Deandra Vandaru

# ------------ Nomor 3 -------------

#Input nilai
u_teo = float(input("Nilai ujian teori : "))
u_prak = float(input("Nilai ujian praktek : "))

if u_teo >= 70 and u_prak >= 70:
    print("Selamat, anda lulus!")

elif u_teo >= 70 and u_prak < 70:
    print("Anda harus mengulang ujian praktek.")

elif u_teo < 70 and u_prak >= 70:
    print("Anda harus mengulang ujian teori.")

else:
    print("Anda harus mengulang ujian teori dan praktek.")
