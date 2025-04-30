from collections import defaultdict

class Solution:
    def count(self, s:str):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        return d

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s) 

        l, r = 0, 1
        max_sub = 1
        d = self.count(s[l:r])
        for i in range(1, len(s)):
            if s[i] in d:
                max_sub = max(max_sub, r - l)
                while s[i] in d:
                    d[s[l]] -= 1
                    if d[s[l]] == 0:
                        del d[s[l]]
                    l += 1
                d[s[i]] += 1 
                r += 1
            else:
                d[s[i]] += 1 
                r += 1

        max_sub = max(max_sub, r - l)
        return max_sub
    

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("bbbbbbb", 1)
    ]
    for c, c_true in cases:
        res = sol.lengthOfLongestSubstring(c) # Run solution func
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")