# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

# Empty positions are marked ..
# Walls are marked W.
# Start and exit positions are empty in all test cases.

#SOLUTION HERE
from collections import deque
def path_finder(maze):
    grid = [list(row) for row in maze.split('\n')]
    n = len(grid)
    start, end = (0,0), (n-1,n-1)
    
    queue = deque([start])
    visited = {start}
    
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    
    while queue:
        r, c = queue.popleft()
        
        if (r,c)==end :
            return True
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            
            if 0<=nr<=n-1 and 0<=nc<=n-1 and grid[nr][nc]=="." and (nr,nc) not in visited:
                visited.add((nr,nc))
                queue.append((nr,nc))
    return False