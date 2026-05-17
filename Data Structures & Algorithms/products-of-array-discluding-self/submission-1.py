class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res_list = [1 for x in range(nums_len)]

        prev_elems_prod = 1
        for i in range(nums_len):
            res_list[i] = res_list[i] * prev_elems_prod
            prev_elems_prod *= nums[i]
        
        after_elems_prod = 1
        for i in range(nums_len-1, -1, -1):
            res_list[i] = res_list[i] * after_elems_prod
            after_elems_prod *= nums[i]

        return res_list