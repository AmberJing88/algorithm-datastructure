#Back tracking
"""1091 shortest path in binary matrix, in an NxN square grid, each cell is either empty'0' or blocked'1'
a clear path from top-left to bottom right has length k, if and only if it is composed of cells c1,c2..ck
such that adjacent cell ci and ci+1 are connected 8-directions."""
def shortestPathBinary(self,grid):
    if not grid or len(grid)==0 or len(grid[0])==0:
        return -1
    n = len(grid)
    if grid[0][0]==1 or grid[n-1][n-1]==1:
        return -1
    q = [(0,0,1)]
    for i, j, d in q:
        if i==n-1 and j==n-1:
            return d
        for x,y in [(i-1,j)(i+1,j),(i,j-1),(i,i+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]:
            if 0 <=x<n and 0<=y<n and grid[x][y]==0:
                grid[x][y] =1
                q.append((x,y,d+1))
    return -1
# method2 :A* search
class Solution:
    def shortestPath(self,grid):
        if not grid or len(grid)==0 or len(grid[0])==0: return -1
        shortest_path = a_star_search(start=(0,0),goal_function=get_goal_function(grid),
        successor_function=get_successor_fuction(grid),heuristic=get_heuristic(grid))
        if shortest_path is None or grid[0][0]==1:
            return -1
        else:
            return len(shortest_path)

    def a_star_search(self,goal_function,success_function,heuristic):
        visited,came_from=set(), dict()
        distance, frontier = {start:0}, PriorityQueue()
        feontier.add(start)
        while frontier:
            node = frontier.pop()
            if node in visited: continue
            if goal_function(node):
                return reconstruct_path(came_from,start,node)
            visited.add(node)
            for successor in successot_function(node):
                frontier.add(successor,priority=distance[node]+1+heuristic(successor))
                if successor not in distance or distance[node]+1<distance[successor]:
                    distance[successor]=distance[node]+1
                    came_from[successor] = node
        return None

    def reconstruct_path(came_from,start,end):
        reverse_path = [end]
        while end!= start:
            end = came_from[end]
            reverse_path.add(end)
        return list(reverse(reverse_path))

    def get_goal_function(grid):
        m,n = len(grid), len(grid[0])
        def is_bottom_right(cell):
            return cell==(m-1,n-1)
        return is_bottom_right

    def get_successor_fuction(grid):
        def get_clear_adjacent_cells(cell):
            i,j = cell
            return ((i+a,j+b) for a in (-1,0,1) for b in (-1,0,1)
            if a!=0 or b !=0
            if 0 <=i+a <len(grid) if 0 <=j+b <len(grid[0])
            if grid[i+1][j+b]==0)
        return get_clear_adjacent_cells

    def get_heuristic(grid):
        m,n = len(grid), len(grid[0])
        (a,b) = goal_cell = m-1,n-1
        def get_clear_path_distance_form_goal(cell):
            (i,j) = cell
            return max(abs(a-i), abs(b-j))
        return get_clear_path_distance_form_goal
from heapq import heappush, heappop
class PriorityQueue:
    def __init__(self,iterable=[]):
        self.heap = []
        for value in iterable:
            heappush(self.heap,(0,value))

    def add(self,value,priority=0):
        heappush(self.heap,(priority, value))

    def pop(self):
        priority,value = heappop(self.heap)
        return value
