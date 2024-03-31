nama_awal = "yusuf"
nama_tengah = "tengah"
nama_akhir = "akhir"

nama_lengkap = nama_awal + " " + nama_tengah +"'" + nama_akhir
print(nama_lengkap)

panjang = len(nama_lengkap)
print(panjang)
print("panjang dari " +  nama_lengkap + " = " + str(panjang))

y = "z"

status = y in nama_lengkap
print(status)

status = y not in nama_lengkap
print(status)