from typing import List


def index_of_sum_numbers(nums: List[int], target: int) -> list:
    length: int = len(nums)
    result: list = []
    for i in range(length):
        for j in range(1, length):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
                return result


print(index_of_sum_numbers(nums=[2, 7, 11, 15], target=9)) # [0, 1]
print(index_of_sum_numbers(nums=[3, 2, 4], target=6)) # [1, 2]
print(index_of_sum_numbers(nums=[3, 3], target=6)) # [0, 1]
