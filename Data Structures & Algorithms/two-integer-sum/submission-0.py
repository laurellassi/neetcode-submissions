class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, number in enumerate(nums):
            value = nums[index]
            complement = target - value

            if complement not in seen:
                seen[value] = index
            else: 
                return [seen[complement], index]

        return []



