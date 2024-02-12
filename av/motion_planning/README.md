## Motion Planning
to find minimum cost path by expanding to next node.

### Search
#### A* search 
- heuristic function is to estimate the cost to reach goal(no need to be accurate, as long as h(x,y) <= distance to goal from x,y)
- open list holds position (x,y), g value and f value(cost value + heuristic value)

#### dynamic programming
it maps coordinates to policy matrix.
