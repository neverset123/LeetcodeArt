# h的值全部为0,A star算法退回到普通搜索算法
#heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

def search_A_star(grid,init,goal,cost):
    # check if cell is used before
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
 
    # record steps from start position
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
 
    x = init[0]
    y = init[1]
    g = 0 
    h = heuristic[x][y]
    f = g + h
 
    open = [[f, g, h, x, y]]
 
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    count = 0
 
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            f = next[0]
            g = next[1]
            h = next[2]
            x = next[3]
            y = next[4]
 
            expand[x][y] = count
            count += 1
 
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost[i]
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2,  x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
 
 
    for i in range(len(expand)):
        print(expand[i])
 
    policy = [['0'  for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    path = [[x,y]]
    policy[x][y] = '*'
    while x!= init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        policy[x2][y2] = delta_name[action[x][y]]
        x = x2
        y = y2
        path.append((x,y))
 
    for i in range(len(policy)):
        print(policy[i])
    path.reverse()
    return expand
 
if __name__ == '__main__':
    # find shortest path with A star algorithm
    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = [2, 2, 1, 1]
    
    delta = [[-1, 0], # go up
            [ 0,-1], # go left
            [ 1, 0], # go down
            [ 0, 1]] # go right
    
    delta_name = ['^', '<', 'v', '>']
    result = search_A_star(grid,init,goal,cost)