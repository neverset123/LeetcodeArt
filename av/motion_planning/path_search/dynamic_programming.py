# policy without heading
def optimum_policy(grid,goal,cost):
    m=len(grid)
    n=len(grid[0])
    value = [[99]*n for _ in range(m)] # heuristic value (distance to goal), 99 means impossible to reach goal
    policy = [[' ']*n for _ in range(m)] # policy map of movement direction
    change = True # flag to indicate if there is any change in value

    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        policy[x][y] = '*'
                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost
                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]          
    return policy

# policy with heading
def optimum_policy2D(grid,init,goal,cost):
    m=len(grid)
    n=len(grid[0])
    # action has 3 values: right turn, no turn, left turn
    action = [-1, 0, 1]
    action_name = ['R', '#', 'L']
    forward = [[-1,  0], # go up
            [ 0, -1], # go left
            [ 1,  0], # go down
            [ 0,  1]] # go right
    forward_name = ['up', 'left', 'down', 'right']
    #四组value值，表示四个不同起始方向
    value = [[[999 for row in range(n)] for col in range(m)],
             [[999 for row in range(n)] for col in range(m)],
             [[999 for row in range(n)] for col in range(m)],
             [[999 for row in range(n)] for col in range(m)]]
    policy = [[[' ' for row in range(n)] for col in range(m)],
             [[' ' for row in range(n)] for col in range(m)],
             [[' ' for row in range(n)] for col in range(m)],
             [[' ' for row in range(n)] for col in range(m)]]
    policy2D = [[' ' for row in range(n)] for col in range(m)]
    change = True
    while change:
        change = False
        for x in range(m):
            for y in range(n):
                for orientation in range(4):
                    if goal[0] == x and goal[1] == y:
                        if value[orientation][x][y] > 0:
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                            change = True
 
                    elif grid[x][y] == 0:
                        for i in range(3): # action has 3 values: right turn, no turn, left turn
                            o2 = (orientation + action[i])%4 # -1%4=3
                            x2 =x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            if x2 >= 0 and x2 < m and y2 >= 0 and y2 < n and grid[x2][y2] == 0:
                                v2 = value[o2][x2][y2] + cost[i]
                                if v2 < value[orientation][x][y]:
                                    change = True
                                    value[orientation][x][y] = v2
                                    policy[orientation][x][y] = action_name[i]
    x = init[0]
    y = init[1]
    orientation = init[2]
    policy2D[x][y] = policy[orientation][x][y]
    while policy[orientation][x][y] != '*':
        if policy[orientation][x][y] == '#':
            o2 = orientation
        elif policy[orientation][x][y] == 'R':
            o2 = (orientation -1)%4
        elif policy[orientation][x][y] == 'L':
            o2 = (orientation +1)%4
        x = x + forward[o2][0]
        y = y + forward[o2][1]
        orientation = o2
        policy2D[x][y] = policy[orientation][x][y]
 
    return policy2D

if __name__ == "__main__":
    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1 # the cost associated with moving from a cell to an adjacent one
    delta = [[-1, 0 ], # go up
            [ 0, -1], # go left
            [ 1, 0 ], # go down
            [ 0, 1 ]] # go right
    delta_name = ['^', '<', 'v', '>']
    print(optimum_policy(grid,goal,cost))
    
    grid = [[1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]]
    init = [4, 3, 0] # given in the form [row,col,direction]
                    # direction = 0: up
                    #             1: left
                    #             2: down
                    #             3: right
    goal = [2, 0]
    cost = [2, 1, 20] # a right turn, no turn, and a left turn
    print(optimum_policy2D(grid,init,goal,cost))
