class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        return [nums[x%nums_len] for x in range(nums_len*2)]