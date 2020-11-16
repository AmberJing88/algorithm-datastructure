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

#279
"""279; perfect squares, given a positive integer n, find teh least number of perfect squares
numbers for example 1,4, 9,16,25... while sum to n."""
# lagrange's four-square theorem
def numSquares(n):
    while True:
        d, m = divmod(n,4)
        if m:
            break
        else:
            n =d
    if n%8==7:
        return 4
    elif (n**0.5).is_integer():
        return 1
    else:
        squares =[i**2 for i in range(1, int(n**0.5+1))]
        i,j = 0, len(squarew) -1
        while i <=j:
            s = squares[i] + squares[j]
            if s<n:
                i+= 1
            elif s>n:
                j -= 1
            else:
                return 2
        else:
            return 3
# BFS method2
def numSquares(n):
    if n<2:
        return n
    lst = []
    i = 1
    while i*i <=n:
        lst.append(i*i)
        i += 1
    cnt = 0
    tocheck = {n}
    while tocheck:
        cnt += 1
        temp = set()
        for x in tocheck:
            for y in lst:
                if x==y:
                    return cnt
                if x<y:
                    break
                temp.add(x-y)
        tocheck = temp
    return cnt

#127
"""127; word ladder,given two words and a dictionary word list, find the length of shortest transformation
sequence from begain ro end word,such that only one letter can be changed at a time. each transformed word
must exist in the word list. """
from collections import defaultdict
def numlength(beginword, endword, wordlist):
    if not beginword or not endword or endword not in wordlist:
        return 0
    L = len(beginword)
    all_dict = defaultdict(list)
    for word in wordlist:
        for i in range(L):
            all_dict[word[:i]+'*'+word[i+1:]].append(word)
    q = collections.dequeue([beginword,1])
    visited = {beginword:True}
    while q:
        c_word, level = q.popleft()
        for in range(L):
            intermediate_word=c_word[:i]+'*'+c_word[i+1:]
            for word in all_dict[intermediate_word]:
                if word==endword:
                    return level+1
                if word not in visited:
                    visited[word] = True
                    q.append((word,level+1))
            all_dict[intermidiate_word]=[]
    return 0
#BFS method
from collections import dequeue
def ladderLenth(beginword, endword, wordlist):
    if not beginword or not endword or endword not in wordlist:
        return 0
    def construct_dict(wordlist):
        d = {}
        for word in wordlist:
            for i in len(word):
                s = word[:i]+'*'+word[i+1:]
                d[s] = d.get(s,[]) + [word]
        return d
    def bfs(begin, end, dict_word):
        q, visited = dequeue([(beigin,1)]), set()
        while q:
            word, steps = q.popleft()
            if word not in visited:
                if word==end:
                    return steps
                visited.add(word)
                for i in range(len(word)):
                    s = word[:i]+'*'+word[i+1:]
                    neigh_words = dict_word.get(s,[])
                    for neign in neigh_words:
                        if neigh not in visited:
                            q.append((neigh,steps+1))
        return 0
    d = construct_dict(set(wordlist) | set([beginword,endword]))
    return bfs(beginword, endword,d)

#785
"""785; is graph bipartite, undirected graph, return true if and only if it is bipartite. recall
we can split a graph 's nodes into two different independent subsets. a and b, and every edge in
the graph has one node in a and another in b."""
# dye method, two points at one edge has different color
def isBipartite(graph):
    colors= [0]* len(graph)
    def valid(graph,color,curr,colors):
        if colors[curr] !=0:
            return colors[curr] == color
        colors[curr] = color
        for i in graph[curr]:
            if not valid(graph,-1*color,i, colors):
                return False
        return True
    for i in range(len(graph)):
        if colors[i]==0 and not valid(graph,1,i,color):
            return False
    return True

#iteration bfs
def isBipartite(graph):
    colors = [0] * len(graph)
    for i in raneg(len(graph)):
        if colors[i] != 0: continue
        queue, colors[i] = [i], 1
        while queue:
            t = queue.pop(0)
            for a in graph[t]:
                if colors[a] ==colors[t]:
                    return False
                if colors[a] ==0:
                    colors[a] = -1 * colors[t]
                    queue.append(a)
    return True

# unionFind method
def isBipartite(graph):
    root = [0]* len(graph)
    for i in range(len(graph)):
        root[i] = i
    def find(root,i):
        if root[i]==i:
            return i
        return find(root,root[i])
    for i in range(len(graph)):
        if not graph[i]: continue
        x, y = find(root,i), find(root, graph[i][0])
        if x==y:
            return False
        for j in range(len(graph[i])):
            parent = find(root, graph[i][j])
            if x ==parent:
                return False
            root[parent] = y
    return True

#207
"""207; course schedule, numcourses, unlabeled from 0 to len(numcourse)-1, some may have prereuist,
like: to take course 0, you have to first finish course 1, which is [0,1]. given the total number of
courses and a list of prereuist pairs, is it possible for you to finish all courses."""
def canFinish(numcourse, prerequisites):
    graph = [[] for _ in range(numcourse)]
    visit = [0 for _ in range(numcourse)]
    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visit[i]==-1:
            return False
        if visit[i] ==1:
            return True
        visit[i]= -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numcourse):
        if not dfs(i):
            return False
    return True

# BFS method
def canFinish(numcourse, prerequisites):
    graph = {i:set() for i in range(numcourse)}
    indeg = {i:0 for i in range(numcourse)}
    for s,e in set(tuple(x) for x in prerequisites):
        graph[s] |= {e}
        indeg[e] +=1
    queue = {i for i in range(numcourse) if not indeg[i]}
    visits = set(queue)
    for node in queue:
        for neigh in graph[node]:
            if neigh in visits:
                return False
            indef[neigh] -= 1
            if not indeg[neigh]:
                visits.add(neigh)
                queue += [neigh]
    return len(visits)==numcourse

#210
"""210; course schdule II, 0~n-1 are labeled courses, prerequisites[i] = [a,b] means a, and b are
prerequiste of course i.given the total number of courses and a list of prereuist pairs, is it
possible for you to finish all courses."""
def findOrder(num, prerequiste):
    res = []
    graph = [[] for _ in rane(num)]
    visit = [0 for _ in range(num)]
    for x,y in prerequiste:
        graph[x].append(y)

    def dfs(i,graph,visit):
        if visit[i]==-1:
            return False
        if visit[i]==1:
            return True
        visit[i] =-1:
        for j in graph[i]:
            if not dfs(j,graph,visit):
                return False
        visit[i] = 1
        res.append(i)
        return True
    for i in range(num):
        if not dfs(i,graph,visit):
            return []
    if len(res) != num:
        return []
    return res

#BFS method2
from collections import defaultdict
def findOrder(num, prerequiste):
    parent = defaultdict(set)
    child = defaultdict(set)
    for i, j in prerequiste:
        parent[i].add(j)
        children[j].add(i)
    bfs = [i for i in range(num) if not parent[i]]
    for i in bfs:
        if parent[i]:
            return []
        for j in child[i]:
            parent[j].remove(i)
            if not parent[j]:
                bfs += [j]
    return bfs if len(bfs)==num else []
