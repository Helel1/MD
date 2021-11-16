def find_smallest(arr):
    smallest_arr = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_arr:
            smallest_arr = arr[i]
            smallest_index = i
        else:
            continue
    return smallest_index

    

