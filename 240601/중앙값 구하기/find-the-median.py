input_list = input()
input_num_list = list(map(int, input_list.split()))
a, b, c = input_num_list

if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c

print(median)