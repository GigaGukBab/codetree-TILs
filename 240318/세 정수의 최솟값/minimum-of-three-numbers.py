num_arr = input()
num_arr = list(map(int, num_arr.split()))
a, b, c = num_arr[0], num_arr[1], num_arr[2]

if a < b and a < c:
    min_val = a
elif b < a and b < c:
    min_val = b
elif c < a and c < b:
    min_val = c

print(min_val)