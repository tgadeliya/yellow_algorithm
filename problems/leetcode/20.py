


class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) == 1:
            return False
        stack = []
        for b in s:
            if b in "({[":
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                e = stack.pop()
                if not ((b == ")" and e == "(") or (b == "}" and e == "{") or (b == "]" and e == "[")):
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False