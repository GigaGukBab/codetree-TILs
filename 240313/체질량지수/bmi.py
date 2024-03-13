nums = input()

num_list = list(map(int, nums.split()))

height, weight = num_list[0], num_list[1]

height_meter = height / 100
bmi = weight // (height_meter**2)

print(int(bmi))

if bmi >= 25:
    print("Obesity")