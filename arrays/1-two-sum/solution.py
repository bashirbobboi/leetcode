from typing import List, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Tuple[int, int]:
        index = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in index:
                return index[find], i
            index[num] = i
