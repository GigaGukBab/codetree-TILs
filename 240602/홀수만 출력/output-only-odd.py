input_num_list = input()

a, b = list(map(int, input_num_list.split()))

for i in range(a, b+1, 2):
    print(i, end=" ")