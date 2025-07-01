class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        nd = []
        rem = 1
        for d in digits[::-1]:
            if d < 9:
                nd.append(d+rem)
                rem = 0
            elif d == 9:
                if rem == 1:
                    nd.append(0)
                else:
                    nd.append(9)
        
        if rem == 1:
            nd.append(1)
        
        return nd[::-1]