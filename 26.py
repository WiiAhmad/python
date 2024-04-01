 #continue pass or break

angka = 0

#while angka < 5:
    #angka += 1
    #if angka == 3:
        #print("test 3")
        #pass
    #print(angka)

while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")

    if angka == 3:
        print("angka sekarang adalah 3")
        continue #loncat kedalam loop selanjutnya
    
    print("lanjut")
    