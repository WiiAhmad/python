koor_katak = int(input("Masukan koordinat katak : "))
lompatan_kanan = int(input("masukan lompatan katak ke kanan : "))
lompatan_kiri = int(input("masukan lompatan katak ke kiri : "))
hasil = koor_katak
i = 0

if koor_katak % 2 == 0 or koor_katak < 0:
    if koor_katak % 3 == 0:
        print("koor katak : kelipatan 3")
        loop = lompatan_kiri * 2
    else:
        loop = lompatan_kanan * lompatan_kiri
    print("koor katak adalah genap")
    print(f"loop adalah : {loop}")
    while i < loop:
        print(f"i sekarang adalah : {i}")
        if i % 2 == 0:
            hasil = hasil + lompatan_kanan
            print(f"hasil dari kanan : {hasil}")
            i+=1
            if i == loop:
                break
        elif i % 2 == 1:
            hasil = hasil - lompatan_kiri
            print(f"hasil dari kiri : {hasil}")
            i+=1
            if i == loop:
                break

elif koor_katak % 2 == 1:
    print("koor katak adalah ganjil")
    loop = lompatan_kanan * 2
    print(f"loop adalah : {loop}")
    while i < loop:
        print(f"i sekarang adalah : {i}")
        if i % 2 == 0:
            hasil = hasil + lompatan_kanan
            print(f"hasil dari kanan : {hasil}")
            i+=1
            if i == loop:
                break
        elif i % 2 == 1:
            hasil = hasil - lompatan_kiri
            print(f"hasil dari kiri : {hasil}")
            i+=1
            if i == loop:
                break



