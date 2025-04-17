
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mds = []
        res = [0] * len(temperatures) 
        mds.append((temperatures[0], 0))
        for idx, t in enumerate(temperatures[1:], 1):
            while mds and t > mds[-1][0]:
                _, i = mds.pop()
                res[i] = idx - i
            mds.append((t, idx))
        return res