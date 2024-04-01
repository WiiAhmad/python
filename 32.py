## menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

c = a.copy()
print(f"c = {c}")
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")