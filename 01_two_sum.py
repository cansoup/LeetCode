class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_one = 0
        index_two = 0
        
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_one = i
                    index_tow = j
                    return [i, j]
