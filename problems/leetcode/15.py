from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numss = sorted(nums)
        viewed = set()

        for k in range(len(numss)-2):
            i, j = k+1, len(numss) - 1
            while i < j:            
                nss = [numss[i], numss[j], nums[k]] 
                if sum(nss) < 0:
                    i += 1
                elif sum(nss) > 0:
                    j -= 1
                else:
                    viewed.add(tuple(sorted(nss)))
        return list(viewed)

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([1,2,-2,-1], []),
        ([0,0,0], [[0,0,0]]),
        ([0,1,1], []),
        ([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10], [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]),
        # ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
    ]
    for c, c_true in cases:
        res = sol.threeSum(c)
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")