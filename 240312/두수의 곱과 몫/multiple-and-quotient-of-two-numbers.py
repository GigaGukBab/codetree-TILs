input_arr = input()

a, b = input_arr.split()[0:2]
a = int(a)
b = int(b)

print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a//b}")