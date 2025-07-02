class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global res
        res = []
        candidates.sort()

        def bt(cand, t, curRes):
            # print(f"{cand=}, {t=}, {curRes=}")
            if t == 0:
                # print(f"{curRes=}")
                curt = tuple(sorted(curRes))
                if curt not in res:
                    res.append(curt)
                return curRes
            else:
                for c in cand:
                    if t-c < 0:          
                        break
                    bt(cand, t-c, curRes + [c])

        bt(candidates, target, [])
        return res