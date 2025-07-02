class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i, s, runl):
            if s == target:
                res.append(runl.copy())
                return

            for idx in range(i, len(candidates)):
                if idx>i and candidates[idx] == candidates[idx-1]:
                    continue
                if s+candidates[idx] > target:
                    break
                
                runl.append(candidates[idx])
                dfs(idx+1, s+candidates[idx], runl)
                runl.pop()

        dfs(0, 0, [])
        return res