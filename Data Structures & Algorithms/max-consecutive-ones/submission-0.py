class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_counter = 0
        for x in nums:
            if x == 0:
                counter = 0
            else:
                counter += 1
            if counter > max_counter:
                max_counter = counter
        return max_counter