"""
1 - 31
2 - 28
3 - 31
4 - 30
5 - 31
6 - 30
7 - 31
8 - 31
9 - 30
10 - 31
11 - 30
12 - 31
"""

n = int(input())

if n % 2 == 1: 
    print(31)
else:
    if n == 2:
        print(28)
    elif n <= 8 or n >= 12:
        print(31)
    else:
        print(30)