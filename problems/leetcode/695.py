class Solution:
    def get_neighbours(self, i, j, grid):
        res = []
        for i,j in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if i <0 or j <0:
                continue
            if i >= len(grid) or j >= len(grid[0]):
                continue 
            res.append((i,j))
        return res

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    #start BFS
                    level = [[(i,j)]]
                    while len(level[-1]) > 0:
                        level.append([])
                        for v in level[-2]:
                            for u in self.get_neighbours(v[0], v[1], grid):
                                if grid[u[0]][u[1]] == 1:
                                    grid[u[0]][u[1]] = 0
                                    area += 1
                                    level[-1].append(u)
                    max_area = max(area, max_area)
        return max_area
    

    
if __name__ == "__main__":
    sol = Solution()
    cases = [
        [[[0,0,1,0,0,0,0,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,1,1,0,1,0,0,0,0,0,0,0,0],
          [0,1,0,0,1,1,0,0,1,0,1,0,0],
          [0,1,0,0,1,1,0,0,1,1,1,0,0],
          [0,0,0,0,0,0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,0,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,1,1,0,0,0,0]], 6]
    ]
    for c, c_true in cases:
        res = sol.maxAreaOfIsland(c) # Run solution func
        assert res == c_true, f"{res} and {c_true}"
    print("Microtests passed!")