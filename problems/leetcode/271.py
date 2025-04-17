from typing import List

class Solution:
    delim = "#"
    def encode(self, strs: List[str]) -> str:
        ns = ""
        for s in strs:
            ns += f"{len(s)}{self.delim}" + s
        return ns

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            code_len = 0  # get new word_len
            while s[i+code_len] != self.delim:
                code_len += 1
            word_len = int(s[i:i+code_len]) # -1 to trim delimiter
            i += code_len + 1 # number str len and delim len
            word = s[i:i+word_len]
            strs.append(word)
            i += word_len # update start of new code
        return strs    

if __name__ == "__main__":
    sol = Solution()
    cases = [["hello", "world"], ["Great", "Gig#", "i#n#", "t#h#e#", "sky"]]
    for c in cases:
        s = sol.encode(c)
        c_decoded =sol.decode(s)
        assert all([p[0] == p[1] for p in zip(c, c_decoded)])
    print("Microtests passed!")