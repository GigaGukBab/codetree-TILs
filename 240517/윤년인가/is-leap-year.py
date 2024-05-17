y = int(input())

if (y % 4 == 0):
    print("true")
elif (y % 4 == 0 and y % 400 == 1):
    print("false")