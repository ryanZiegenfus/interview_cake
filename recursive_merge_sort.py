def rec_func(arr):
    #bottom condition
    if len(arr) == 1:
        return arr
    # splitting the array in half        
    middle = int(len(arr) / 2)
    left = rec_func(arr[:middle])
    right = rec_func(arr[middle:])
    # recombine and sort array
    temp_arr = left + right
    sorted_arr = []
    for x in range(0, len(temp_arr)):
        lowest = temp_arr[0]
        for i in temp_arr:
            if i < lowest:
                lowest = i
        sorted_arr.append(lowest)
        temp_arr.remove(lowest)
    return sorted_arr

print(rec_func(['z','x','a','b','t']))