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

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] == target:
            return True
        
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        if len(matrix) > 1:
            s = [m[0] for m in matrix] + [float("inf")]
            if target in s:
                return True
            res = -1        
            for i in range(1, len(s)):
                if s[i-1] <= target <= s[i]:
                    res = i-1
        else:
            res = 0

        if res == -1:
            return False
        
        row = matrix[res]
        return False if self.search(row, target) == -1 else True 
    

if __name__ == "__main__":
    sol = Solution()
    cases = [
        [([ [1,3] ], 3), True],
        [([[1],[3]], 3), True],
        [([ [1,3,5,7], [10,11,16,20], [23,30,34,60]], 3), True],
        [([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False]
    ]
    for c, c_true in cases:
        res = sol.searchMatrix(c[0], c[1]) # Run solution func
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")