input_arr = input()
a, b = input_arr.split()[0:2]
a, b = int(a), int(b)

result = (a+b) / (a-b)

print(f"{result:.2f}")