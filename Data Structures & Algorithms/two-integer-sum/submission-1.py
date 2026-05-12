class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ordered_nums = sorted(nums)
        checked_elem = None
        for elem in ordered_nums:
            if elem == checked_elem:
                continue
            try:
                second_elem = ordered_nums[ordered_nums.index(target - elem)]
                first_elem_idx = nums.index(elem)
                return [first_elem_idx, nums.index(second_elem, first_elem_idx+1)]
            except ValueError:
                checked_elem = elem
                continue
            