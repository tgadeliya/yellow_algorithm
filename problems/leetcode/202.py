class Solution:
    def getsq(self, num):
        return sum(int(d) ** 2 for d in str(num))

    def isHappy(self, n: int) -> bool:
        # Lazy to use slow/fast pointers
        combs = {n}
        while True:
            n = self.getsq(n)
            if n in combs or n == 1:
                return n == 1
            combs.add(n)
            
