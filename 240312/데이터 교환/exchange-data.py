a = 5
b = 6
c = 7


tmp1 = a # tmp=5
tmp2 = b # tmp=6
tmp3 = c # tmp=7

a = tmp3 # a = 7
b = tmp1 # b = 5
c = tmp2 # c = 6

print(a) # 7
print(b) # 5
print(c) # 6