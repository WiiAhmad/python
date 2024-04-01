#looping list dan enumerate

#for loop
list = [2,3,4,5,6,7,9,0]

for a in list:
    print(f"a : {a}")

#for loop dan range

panjang = len(list)
print("==============")

for a in range(panjang):
    print(f"a : {list[a]}")

#while
print("==============")

i = 0

while i < len(list):
    print(f"a = {list[i]}")
    i += 1

print("==============")
[print(f"a = {i}") for i in list]

#enumerate dan comprehension