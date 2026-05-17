class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res_list = [1 for x in range(nums_len)]
        for i, elem in enumerate(nums):
            for j in range(nums_len):
                res_list[j] = res_list[j] * (elem if i != j else 1)
        return res_list