num_list = input()
num_list = list(map(int, num_list.split()))
a, b, c = num_list[0], num_list[1], num_list[2]

if a == min(a, b, c):
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b == c:
    print(1, end=" ")
else:
    print(0, end=" ")