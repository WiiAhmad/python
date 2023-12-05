a = 10
b = 7

c = a | b

print('or')

print("nilai :", a, ", binary :", format(a, '08b'))
print("nilai :", b, ", binary :", format(b, '08b'))
print("-------------------------------(|)")
print("nilai :", c, ", binary :", format(c, '08b'))

print('and')
c = a & b
print("nilai :", a, ", binary :", format(a, '08b'))
print("nilai :", b, ", binary :", format(b, '08b'))
print("-------------------------------(&)")
print("nilai :", c, ", binary :", format(c, '08b'))

c = a ^ b
print('xor')
print("nilai :", a, ", binary :", format(a, '08b'))
print("nilai :", b, ", binary :", format(b, '08b'))
print("-------------------------------(^)")
print("nilai :", c, ", binary :", format(c, '08b'))

c = ~a
print('not')
print("nilai :", a, ", binary :", format(a, '08b'))
print("-------------------------------(~)")
print("nilai :", c, ", binary :", format(c, '08b'))
print("-------------------------------(^)")

      