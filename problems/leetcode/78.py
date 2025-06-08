class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]
        for n in nums:
            resc = [r for r in res]
            for r in resc:
                new = r + [n]
                res.append(new)
        return res