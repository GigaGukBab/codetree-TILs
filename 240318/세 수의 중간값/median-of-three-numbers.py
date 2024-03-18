num_arr = input()
num_arr = list(map(int, num_arr.split()))
a, b, c = num_arr[0], num_arr[1], num_arr[2]

if a < b and b < c:
    print(1)
else:
    print(0)