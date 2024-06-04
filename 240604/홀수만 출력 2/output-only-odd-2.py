input_num_list = input()
b, a = list(map(int, input_num_list.split()))

for i in range(b, a-1, -1):
    if i % 2 == 1:
        print(i, end=" ")