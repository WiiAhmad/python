data_integer = 1

print(type(data_integer))
print("data integer:", data_integer , "bertipe data", type(data_integer))

data_float = 1.5
print(type(data_float))
print("data float :", data_float, "bertipe data: ", data_float)

data_string = "string"
print("data string: ", data_string, type(data_string))

# print("data bool:", data_bool, type(data_bool))

from ctypes import c_double

data_c_double = c_double(10.5)
print(data_c_double, type(data_c_double))