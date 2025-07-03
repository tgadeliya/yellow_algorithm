class Solution:
    def add(self, ss: list[str], bef: int) -> tuple[str, int]:
        res = sum(map(int, ss)) + bef
        # print(f"{ss=}, {bef=}, {res=}")
        return res % 10, res // 10  
    
    def mult_one(self, num1: str, d: str) -> str:
        res, per = "", 0 
        for n in num1[::-1]:
            r = int(d) * int(n) + per
            res += str(r % 10)
            per = r // 10
        
        if per > 0:
            res += str(per)
        # print(f"mult {num1=}, {d=}, {res[::-1]=}")
        return res

    def multiply(self, num1: str, num2: str) -> str:
        res = []
        i = 0
        for m in num2[::-1]:
            tmp = "0" * i + self.mult_one(num1, m) 
            res.append(tmp[::-1])
            i += 1
        # print(res)
        # add leading zeros for aligning
        maxl = max(map(len, res))
        res = [(((maxl - len(n)) * "0") + n)[::-1]  for n in res]
        # print(res)

        resf, per = "", 0
        for p in zip(*res):
            res, per = self.add(p, per)
            resf += str(res)
        if per > 0:
            resf += str(per)
        return "0" if "0" in resf and len(set(resf)) == 1 else resf[::-1]