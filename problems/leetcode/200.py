class Solution:
    def return_parent(self,i,j,grid):
        res = []
        len_x = len(grid[0])
        len_y = len(grid)
        for i,j in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if i < 0 or j <0:
                continue
            if i >= len_y or j >= len_x:
                continue
            res.append((i,j))
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        num_groups = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # start BFS
                    level = [[(i,j)]]
                    while len(level[-1]) > 0: 
                        level.append([])
                        for u in level[-2]:
                            for v in self.return_parent(u[0],u[1], grid):
                                if grid[v[0]][v[1]] == "1":
                                    grid[v[0]][v[1]] = "0"
                                    level[-1].append(v)
                    num_groups += 1
        return num_groups