from typing import List



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_set = {"+", "-", "*", "/"}
        vals = []
        
        for t in tokens:
            if t in ops_set:
                n2 = vals.pop()
                n1 = vals.pop() 
                nval = int(eval(n1+t+n2)) # eval and get ceil 
                vals.append(str(nval)) # to str for future eval
            else:
                vals.append(t) 
        
        return int(vals[0]) if len(vals) else 0 