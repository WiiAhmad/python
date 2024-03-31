#percabangan latihan

print("program kalkulator sederhana dengan 2 input")

angka1 = float(input("masukan angka pertama : "))
operator = input("masukan operator : ")
angka2 = float(input("masukan angka kedua : "))

print(f"angka pertama {angka1}, angka kedua {angka2}")

if operator == "+":
    hasil = angka1 + angka2
    print(f"jawaban adalah {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"jawaban adalah {hasil}")