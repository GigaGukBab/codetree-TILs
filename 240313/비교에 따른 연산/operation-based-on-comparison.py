num_arr = input()

num_arr = list(map(int, num_arr.split()))

a, b = num_arr[0], num_arr[1]

if a > b:
    print(a*b)
else:
    print(b//a)