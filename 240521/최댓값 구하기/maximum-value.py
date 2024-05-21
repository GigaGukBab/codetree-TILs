input_num_list = input()
a, b, c = map(int, input_num_list.split())

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else: # b > a
    if b > c:
        print(b)
    else:
        print(c)