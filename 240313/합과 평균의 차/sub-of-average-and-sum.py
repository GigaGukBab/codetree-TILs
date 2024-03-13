in_arr = input()

    in_arr = in_arr.split()

    in_arr = [int(items) for items in in_arr]

    num_sum = sum(in_arr)
    num_avg = sum(in_avg) // len(in_arr)
    num_diff = num_sum - num_avg