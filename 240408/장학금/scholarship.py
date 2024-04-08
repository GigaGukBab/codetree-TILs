"""
중간고사를 90점 이상 받은 자들로 한해서, 기말고사 점수에 따라 장학금을 지급하기로 했습니다. 
기말고사 점수가 100점 만점에 95점 이상은 10만 원, 90점 이상은 5만 원, 그 미만 점수는 받지 못합니다. 
중간, 기말고사 점수를 입력했을 때 받을 수 있는 장학금을 출력하는 프로그램을 작성해주세요.
"""

input_string = input()

numbers = [int(num) for num in input_string.split()]

mid, fin = numbers[0], numbers[1]

if mid >= 90:
    if fin >= 95:
        print(100000)
    elif fin >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)