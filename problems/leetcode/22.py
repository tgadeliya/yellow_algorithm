from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        stack = []
        res = []
        def bt(no, nc):
            if no == nc == n:
                res.append("".join(stack))


            if no < n:
                stack.append("(")
                bt(no+1, nc)
                stack.pop()

            if nc < no:
                stack.append(")")
                bt(no, nc+1)
                stack.pop()
            
        bt(0,0)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    cases = [(3, ["((()))","(()())","(())()","()(())","()()()"])]
    for c, c_true in cases:
        res = sol.generateParenthesis(c)
        assert set(res) == set(c_true), f"{res} and {c_true}"
    print("Microtests passed!")