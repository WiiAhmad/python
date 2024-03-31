#date and time

import datetime as dt
# hari_ini = dt.date.today()
# print(hari_ini)

# tanggal = dt.date(2005,10,10)
# print(tanggal)

print("silahkan masukan tanggal, bulan dan tahun lahir anda")
tanggal = int(input("tanggal \t :"))
bulan = int(input("bulan \t\t :"))
tahun = int(input("tahun \t\t :"))

tanggallahir = dt.date(tahun, bulan, tanggal)
print(tanggallahir)