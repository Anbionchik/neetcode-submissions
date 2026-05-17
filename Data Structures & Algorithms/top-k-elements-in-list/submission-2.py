class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_dict = {}
        for elem in nums:
            if not elem in res_dict.keys():
                res_dict[elem] = 1
            else:
                res_dict[elem] += 1
        return sorted(res_dict, key=res_dict.get)[-k:]