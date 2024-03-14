a = int(input())
bcde = input()
bcde = list(map(int, bcde.split()))
b, c, d, e = bcde[0], bcde[1], bcde[2], bcde[3] 

if a > b:
    print(1)
else:
    print(0)

if a > c:
    print(1)
else:
    print(0)

if a > d:
    print(1)
else:
    print(0)

if a > e:
    print(1)
else:
    print(0)