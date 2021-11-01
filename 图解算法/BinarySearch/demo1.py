from typing import List


def binary_search(num_list: List, item):
    low = 0
    high = len(num_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if num_list[mid] > item:
            high = mid - 1
        elif num_list[mid] < item:
            low = mid + 1
        else:
            return mid
    return None


nums = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(nums, 2))