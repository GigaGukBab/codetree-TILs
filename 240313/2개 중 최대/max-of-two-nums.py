num = input()

num_arr = list(map(int, num.split()))

a, b = num_arr[0], num_arr[1]

print(max(a, b))