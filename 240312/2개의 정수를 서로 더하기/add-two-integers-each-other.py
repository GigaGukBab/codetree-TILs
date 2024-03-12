input_arr = input()

a, b = input_arr.split()[0:2]
a, b = int(a), int(b)

temp = b
a += temp
b += a
print(a, b)