from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        p, q = 0, len(nums) - 1
        while p <= q:
            m = (p + q) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                q = m - 1
            else:
                p = m + 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([[-1,0,3,5,9,12],9], 4),
        ([[-1,0,3,5,9,12], 2], -1)
    ]
    for c, c_true in cases:
        res = Solution().search(c[0], c[1]) # Run solution func
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")