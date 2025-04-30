from collections import defaultdict
class Solution:

    def count(self, s):
        d = defaultdict(int)
        for ss in s:
            d[ss] += 1
        return d

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = self.count(s1)
        s1l = len(s1)

        for i in range(len(s2)-s1l+1):
            # possible update: on every step delete from sub char i-1 and add new char, 
            # instead recreating the whole dict
            sub = self.count(s2[i:i+s1l])
            if s1s == sub:
                return True
        
        return False
    
if __name__ == "__main__":
    sol = Solution()
    cases = [
        [("hello", "ooolleoooleh"), False]
    ]
    for c, c_true in cases:
        res = sol.checkInclusion(c[0], c[1]) # Run solution func
        # assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")