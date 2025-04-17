from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        rows = [[int(bb) for bb in b if bb!="."] for b in board]
        for row in rows:
            if len(row)!= 0 and (min(row) < 0 or max(row) > 9 or len(row) != len(set(row))):
                return False
        # col
        cols = []
        for i in range(len(board[0])):
            col = []
            for b in board:
                if b[i] != ".":
                    col.append(int(b[i]))
            cols.append(col)

        for col in cols:
            if len(col)!= 0 and (min(col) < 0 or max(col) > 9 or len(col) != len(set(col))):
                return False
        # sub-boxes
        for i in range(3):
            for j in range(3):
                sub_board = [b[(3*j):3*(j+1)] for b in board[(3*i):3*(i+1)]]
                sbf = [int(bb) for b in sub_board for bb in b if bb!='.']
                if len(sbf)!= 0 and (len(sbf) != len(set(sbf)) or min(sbf) < 0 or max(sbf) > 9):
                    return False
        return True
    

if __name__ == "__main__":
    sol = Solution()
    cases = [
        ([[".",".",".",".","5",".",".","1","."],
          [".","4",".","3",".",".",".",".","."],
          [".",".",".",".",".","3",".",".","1"],
          ["8",".",".",".",".",".",".","2","."],
          [".",".","2",".","7",".",".",".","."],
          [".","1","5",".",".",".",".",".","."],
          [".",".",".",".",".","2",".",".","."],
          [".","2",".","9",".",".",".",".","."],
          [".",".","4",".",".",".",".",".","."]], False)
    ]
    for c, c_true in cases:
        res = sol.isValidSudoku(c)
        assert res == c_true
    print("Microtests passed!")