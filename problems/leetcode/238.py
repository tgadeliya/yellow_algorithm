from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        post = [1]
        i = 0
        for n in nums[::-1]:
            post.append(post[i]*n)
            i += 1
        post = post[:-1]
        post = post[::-1]
        res = []
        for i in range(len(nums)):
            res.append(pref * post[i])
            pref *= nums[i]
        return res
    

class Solution2:
    """
    Solution with O(1) extra space except output array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = 1
        post = [1]
        i = 0
        for n in nums[::-1]:
            post.append(post[i]*n)
            i += 1
        post = post[-2::-1]
        for i in range(len(nums)):
            post[i] = pref * post[i]
            pref *= nums[i]        
        return post
    

if __name__ == "__main__":
    for solution in [Solution, Solution2]:
        sol = solution()
        cases = [
            ([1,2,3,4],[24, 12 ,8, 6])
        ]
        for c,c_true in cases:
            res = sol.productExceptSelf(c)
            assert all([p[0] == p[1] for p in zip(res,c_true)])
        print("Microtests passed!")

    
