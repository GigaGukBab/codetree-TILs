curr_time = input()
h, m = curr_time.split(":")[0:2]
print(f"{int(h)+1}:{int(m)}")