input_num_list = input()
b, a = list(map(int, input_num_list.split()))

while b >= a:
    if b % 2 == 0:
        print(b, end=" ")
    b -= 1