input_arr = input()
input_data_arr_str = input_arr.split() # string type
input_data_arr_int = [int(items) for items in input_data_arr_str] # integar type
print(sum(input_data_arr_int), sum(input_data_arr_int) / len(input_data_arr_int))