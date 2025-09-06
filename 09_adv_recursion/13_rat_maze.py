maze = [[1, 0, 0], 
        [1, 1, 0], 
        [1, 1, 1]]

n = len(maze[0])
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = []

# DLRU

def backtrack(pos_x, pos_y, maze, visited, path):
    if maze[0][0] == 0:
        return
    
    if pos_x < 0 or pos_x >= n or pos_y < 0 or pos_y >= n:
        return
    
    if (pos_x == n-1 and pos_y == n-1): 
        ans.append(path)
        return   

    # down
    if pos_x + 1 < n and (maze[pos_x + 1][pos_y] == 1 and not visited[pos_x + 1][pos_y]):
        visited[pos_x][pos_y] = 1
        backtrack(pos_x + 1, pos_y, maze, visited, path + "D")
        visited[pos_x][pos_y] = 0  

    # left
    if pos_y - 1 >= 0 and (maze[pos_x][pos_y - 1] == 1 and not visited[pos_x][pos_y - 1]):
        visited[pos_x][pos_y] = 1 
        backtrack(pos_x, pos_y - 1, maze, visited, path + "L")
        visited[pos_x][pos_y] = 0  

    # right
    if pos_y + 1 < n and (maze[pos_x][pos_y + 1] == 1 and not visited[pos_x][pos_y + 1]):
        visited[pos_x][pos_y] = 1
        backtrack(pos_x, pos_y + 1, maze, visited, path + "R" )
        visited[pos_x][pos_y] = 0  

    # up 
    if pos_x - 1 >= n and (maze[pos_x][pos_y + 1] == 1 and not visited[pos_x][pos_y + 1]):
        visited[pos_x][pos_y] = 1 
        backtrack(pos_x - 1, pos_y, maze, visited, path + "U" )
        visited[pos_x][pos_y] = 0  

backtrack(0, 0, maze, visited, "")

print(ans)