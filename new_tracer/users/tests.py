from django.test import TestCase

# Create your tests here.
def get_combinations(nums):
    result = []
    backtrack(nums, [], result)
    return result


def backtrack(nums, path, result):
    result.append(path[:])
    for i in range(len(nums)):
        backtrack(nums[i + 1:], path + [nums[i]], result)


# 示例用法
nums = [1, 2, 3]
combinations = get_combinations(nums)
# print(combinations


def huiwen(lst):
    if len(lst) <= 2:
        return True
    elif lst[0] != lst[-1]:
        return False
    return huiwen(lst[1:-1])


str1 = "Runoob example…wow!!!"
str2 = "exam"
# print(str1.find(str2,7))

str = '/projectstar/29/'
print(str.split('/'))

