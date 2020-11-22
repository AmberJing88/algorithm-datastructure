#Back tracking
"""37: sudoku solver, filling the empty cells with 1-9 to each row, eack col and each sub chunks."""
class Solution:
    def solveSudolu(self, board):
        self.board = board
        self.state = {str(x):0 for x in range(1,10)}
        self.initState()
        self.solve()

    def initState(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] !='.':
                    self.state[self.board[row][col]] += 1
    def solve(self):
        row, col = self.findUnassigned()
        if row ==-1 and col == -1:
            return True
        for num in set([x for x in self.state if self.state[x]!=9]):
            if self.isSafe(row, col,num):
                self.board[row][col] = num
                self.state[num] += 1
                if self.solve():
                    return True
                self.board[row][col] ='.'
                self.state[num] -= 1
        return False
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] =='.':
                    return row, col
        return -1,-1
    def isSafe(self,row, col, ch):
        boxrow = 3*(row//3)
        boxcol = 3*(col//3)
        if self.checkrow(row, ch) and self.checkcl(col,ch) and self.checksquare(boxrow,boxcol, ch):
            return True
        return False
    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] ==ch:
                return False
        return True
    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] ==ch:
                return False
        return True
    def checksquare(self,row, col, ch):
        for r in range(row, row+3):
            for c in range(col, col+3):
                if self.board[r][c] ==ch:
                    return False
        return True

#51
"""51: N queens, on N*N board set n queens each one line one col and diagnals."""
class NQueens:
    def solveNqueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums,index):
                temp = '.'* len(nums)
                self.dfs(nums, index+1, path+temp[:i]+'Q'+temp[i+1:],res)

    def valid(self, nums, index):
        for i in range(index):
            if abs(nums[i]-nums[index])==index-i or nums[i]==nums[index]:
                return False
        return True

#695
"""695: max area of island, 2d-array, of 0 (sea) and 1 (island) connected 4-directions. find the maxmum area of
an island in the 2D array. """
def maxAreaIsland(grid):
    res = 0
    m,n = len(grid), len(grid[0])
    def DFS(grid, i, j):
        if i <0 or i >=m or j<0 or j>=n or grid[i][j]==0:
            return 0
        grid[i][j]=0
        area = 1
        direction = [(1,0), (-1,0),(0,1),(0,-1)]
        for d in direction:
            area += DFS(grid, i+d[0],j+d[1])
        return area
    for i in range(m):
        for j in range(n):
            res = max(res, DFS(grid,i,j))
    return res
#200
"""200 2D grid map, '1' is connected island and '0'is water, count the number of islands"""
def numIsland(grid):
    res = 0
    if not grid: return 0
    m,n = len(grid), len(grid[0])
    def DFS(grid,i,j):
        if i <0 or i >=m or j<0 or j>=n or grid[i][j] =='0':
            return
        grid[i][j] = '0'
        DFS(grid,i+1, j)
        DFS(grid,i-1, j)
        DFS(grid,i, j+1)
        DFS(grid,i, j-1)
    for i in range(m):
        for j in range(n):
            if grid[i][j] =='1':
                DFS(grid,i,j)
                res += 1
    return res

# unifind method
class SOlution:
    def numIslands(self,grid):
        if not grid or len(grid)==0 or len(grid[0])==0: return 0
        uf = UnionFind(grid)
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] =='1':
                    for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                        x, y = i +d[0], j+d[1]
                        if x >=0 and x<m and 0<=y<n and grid[x][y]=='1':
                            id1, id2 = i*n+j, x*n+y
                            uf.Union(id1, id2)
        return us.count
class UnionFind:
    def UnionFind(self, grid):
        m,n = len(grid), len(grid[0])
        self.father = {}
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    id = i*n +j
                    self.father[id]=id
                    self.count += 1
    def Union(self,node1,node2):
        find1 = self.find(node1)
        find2 = self.find(node2)
        if find1 != find2:
            self.father[find1] = find2
            self.count += 1
    def find(self, node):
        if self.father[node] ==node:
            return node
        father[node] = self.find(father[node])
        return father[node]

#547
"""547; friends dircle, N students, if a is direct friend of B, b is direct friends of c,
a is indirect friends of c, a b,c in a circle. find out how many friends circles in a group"""
def findCircleNum(M):
    if not M or len(M)==0:
        return 0
    count = 0
    seen =set()
    def dfs(row):
        for idx, relation in enumerate(M[row]):
            if relation and idx not in seen:
                seen.add(idx)
                dfs(idx)
        for row in range(len(M)):
            if row not in seen:
                dfs(row)
                count += 1
    return count

#130
"""130;surrounded regions:given 2D grid, containing 'x' blocks and '0' path, captured and fliping
all regions '0' to 'x', that surrounded. boarder '0' no need to change"""
def solve(board):
    if not board or len(board)==0 or len(board[0])==0:
        return
    m,n = len(board), len(board[0])
    def dfs(board, i, j):
        if board[i][j]=='0':
            board[i][j]='#'
        if i >0 and board[i-1][j]=='0':
            dfs(board,i-1,j)
        if i<m-1 and board[i+1][j]=='0':
            dfs(board,i+1,j)
        if j>0 and board[i][j-1]=='0':
            dfs(board,i, j-1)
        if j <n-1 and board[i][j+1]=='0':
            dfs(board,i, j+1)
    for i in raneg(m):
        for j in range(n):
            if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='0':
                dfs(board,i,j)
    for i in range(m):
        for j in range(n):
            if board[i][j]=='0':
                board[i][j] ='x'
            if board[i][j]=='#':
                board[i][j]='0'

#417
"""417; mxn matrix representing height of land, the pacific (left and top) and atlantic
(right and bottom) waters edge.water can flow flip directions from cell higher or equal to lower
find the list grid coordinates where water can flow both oceans."""
def PacificAtlantic(matrix):
    if not matrix or len(matrix)==0 or len(matrix[0])==0:
        return []
    res, m,n = [], len(matrix), len(matrix[0])
    pacific = [[False for _ in range(n)] for _ in range(m)]
    atlantic = [[False for _ in range(n)] for _ in range(m)]

    def dfs(matrix, visited, pre, i, j):
        if i <0 or i >=m or j<0 or j>=n or visited[i][j] or matrix[i][j]<pre:
            return
        visited[i][j]= True
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for d in directions:
            dfs(matrix, visited, matrix[i][j],i+d[0],j+d[1])
    for i in range(m):
        dfs(matrix, pacific,-1,i,0)
        dfs(matrix,atlantic,-1,i,n-1)
    for j in range(n):
        dfs(matrix, pacific,-1,0,j)
        dfs(matrix,atlantic,-1,m-1,j)
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]
            res.append((i,j))
    return res
