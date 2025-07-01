class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
        
        if text1[0] == text2[0]:
            res[0][0] = 1

        for i in range(1, len(text1)):
            res[0][i] = max(res[0][i-1], int(text1[i] == text2[0]))

        for j in range(1, len(text2)):
            res[j][0] = max(res[j-1][0], int(text2[j] == text1[0]))


        for i in range(1, len(text2)):
            for j in range(1, len(text1)):
                res[i][j] = max(res[i][j-1], res[i-1][j], res[i-1][j-1] + int(text2[i] == text1[j]))
        return res[-1][-1]