num_arr = input()
num_arr = list(map(int, num_arr.split()))
a, b, c = num_arr[0], num_arr[1], num_arr[2]

if a > b:
    min_val = b
else:
    min_val = a

if b > c:
    min_val = c
else:
    min_val = b

if c > b:
    min_val = b
else:
    min_val = c

print(min_val)