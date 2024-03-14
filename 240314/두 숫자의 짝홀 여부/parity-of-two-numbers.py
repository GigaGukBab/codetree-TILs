input_arr = input()

input_arr = list(map(int, input_arr.split()))

a, b = input_arr[0], input_arr[1]

if a % 2 == 0:
    print("even")
else:
    print("odd")

if b % 2 == 0:
    print("even")
else:
    print("odd")