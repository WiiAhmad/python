#break

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang = {angka}")

    if angka == 3:
        print("break")
        break

    print("loop")

print("finish")