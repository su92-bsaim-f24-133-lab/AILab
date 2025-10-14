from collections import deque  


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    
    g_score = {start: 0}  # Distance from start
    f_score = {start: heuristic(start, goal)}  # g + h
    came_from = {}  # To rebuild path
    

    open_set = [(f_score[start], start)]  
    
    while open_set:
        # Get lowest f
        open_set.sort()  
        current_f, current = open_set.pop(0)
        
        if current == goal:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:  # Valid and not wall
                tentative_g = g_score[current] + 1  # Step cost 1
                
                neighbor = (nx, ny)
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # Better path!
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_new = tentative_g + heuristic(neighbor, goal)
                    f_score[neighbor] = f_new
                    open_set.append((f_new, neighbor))
    
    return None  # No path


grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

path = astar(grid, (0, 0), (4, 4))
print("Path found:", path)