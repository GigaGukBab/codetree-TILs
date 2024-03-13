in_arr = input()

a, b = in_arr.split()[0:2]

a, b = int(a), int(b)

if a>b:
    print(a-b)
elif a<b:
    print(b-a)
else:
    print("both are the same number")