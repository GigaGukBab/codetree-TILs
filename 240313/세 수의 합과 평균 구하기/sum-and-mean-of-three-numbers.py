in_arr = input()

in_arr = in_arr.split()

in_arr = [int(items) for items in in_arr]

numSum  = sum(in_arr)
print(numSum)

numAvg = numSum // len(in_arr)
print(numAvg)