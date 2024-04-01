#copy 2d list

data1 = [0,1]
data2 = [2,3]

data2d = [data1, data2]

print(f"data 2d : {data2d}")

#deep copy
from copy import deepcopy
data2dcopy = deepcopy(data2d)

print(f"data 2 d deep copy : {data2dcopy}")
print(f"address data2d : {hex(id(data2d))}")
print(f"address data2d : {hex(id(data2dcopy))}")