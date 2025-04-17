from typing import List
from collections import defaultdict

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         nums_set = set(nums)

#         seqs_can_start = [num for num in nums_set if ((num - 1) not in nums_set) and (num+1 in nums_set)]
#         lcs = 1
#         for elem in seqs_can_start:
#             n = elem
#             t = 1
#             while n+1 in nums_set:
#                 n+=1
#                 t+=1        
#             lcs = max(lcs, t)
#         return lcs

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res

if __name__ == "__main__":
    sol = Solution()
    cases = [ ([0, -1], 2), ([0,3,7,2,5,8,4,6,0,1], 9), ([1,0,1,2], 3),]
    for c, c_true in cases:
        res = sol.longestConsecutive(c)
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")