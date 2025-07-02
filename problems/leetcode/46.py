class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(pos_idx, arr, ignore):
            # print(f"{pos_idx=}, {arr=}, {ignore=}")
            if pos_idx == len(nums):
                res.append(arr)
                return

            for i in range(len(nums)):
                if i not in ignore:
                    dfs(pos_idx+1, arr + [nums[i]] , ignore + [i])
            return

        dfs(0, [], [])
        return res