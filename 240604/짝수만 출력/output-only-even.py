input_num_list = input()
a, b = list(map(int, input_num_list.split()))

assert 1 <= a <= b <= 50, "a 또는 b가 범위를 벗어났습니다."
assert a % 2 == 0 and b % 2 == 0, "a 또는 b가 짝수가 아닙니다."

while a <= b:
    if a % 2 == 0:
        print(a, end=" ")
    a+=1