input_num_list = input()
a, b = list(map(int, input_num_list.split()))

for i in range(b, a-1, -1):
    print(i, end=" ")