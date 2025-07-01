class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]

        return res[-1][-1]
    




    