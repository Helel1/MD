from copy import deepcopy
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """两数之和"""
    nums_temp = sorted(nums)
    li = 0
    r = len(nums) - 1
    while nums_temp[li] + nums_temp[r] != target:
        if nums_temp[li] + nums_temp[r] > target:
            r -= 1
        elif nums_temp[li] + nums_temp[r] < target:
            li += 1

    return sorted([nums.index(nums_temp[li]), nums.index(nums_temp[r], 1 + nums.index(nums_temp[li]))]) if nums_temp[
                                                                                                               li] == \
                                                                                                           nums_temp[
                                                                                                               r] else sorted(
        [
            nums.index(nums_temp[li]), nums.index(nums_temp[r])])


def reverse(x: int) -> int:
    if x >= 2 ** 31 or x < -2 ** 31 or x == 0:
        return 0
    else:
        temp = list(str(abs(x)))
        temp = temp[::-1]
        r = ''.join(temp)

        if x < 0:
            result = -int(r)
            if result < -2 ** 31:
                return 0
            else:
                return result
        else:
            result = int(r)
            if result >= 2 ** 31:
                return 0
            else:
                return result


def findWords(words: List[str]) -> List[str]:
    result = []
    for word in words:
        temp = set()
        for i in set(word.lower()):
            if i in "qwertyuiop":
                temp.add('qwertyuiop')
                continue
            if i in "asdfghjkl":
                temp.add("asdfghjkl")
                continue
            if i in "zxcvbnm":
                temp.add('zxcvbnm')
                continue
        if len(temp) > 1:
            continue
        result.append(word)
    return result


def longestCommonPrefix(strs: List[str]) -> str:
    result = []
    for temp in zip(*strs):
        if len(set(temp)) == 1:
            result.append(temp[1])
        else:
            break
    return ''.join(result)


if __name__ == '__main__':
    # print(twoSum([-1, -2, -3, -4, -5], -8))
    # print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(longestCommonPrefix(["flower", "fow", "flight"]))
