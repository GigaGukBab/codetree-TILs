input_arr = input()
input_arr = list(map(int, input_arr.split()))
a, b = input_arr[0], input_arr[1]

if a >= b:
    print(1)
else:
    print(0)

if a > b:
    print(1)
else:
    print(0)

if a <= b:
    print(1)
else:
    print(0)

if a < b:
    print(1)
else:
    print(0)