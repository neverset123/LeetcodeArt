## Motion Planning
to find minimum cost path by expanding to next node. it usually use frenet coordinate(s-longitudinal position along the road, d-lateral position on the road).

### Route Planning Search
#### discrete 
1) A star search 
use heuristic function to find path
- heuristic function is to estimate the cost to reach goal(no need to be accurate, as long as h(x,y) <= distance to goal from x,y)
- open list holds position (x,y), g value and f value(cost value + heuristic value)

2) dynamic programming
search for action policy for each position.

#### continuous

### Prediction
it takes input from map of the world and sensor fusion data, generates state of the world of all vehicles and moving objects. it is represented by state of possible trajectories.
![](../../docs/img/prediction.PNG)
#### Model based approach
use mathmatical model of motion to predict trajectory, which takes account of the physical capabilities of objects as well as the constraints of road and traffic laws etc. advantages are: incorporate knowledges of physics and constrains imposed by road, traffic laws.
process model (physical motion models) + multi-modal estimator (handling uncertainty associated with prediction).
steps: for each dynamic object nearby
- identify common driving behaviors(change lane, turn left, corss street etc)
- define process model for each 
- update beliefs by comparing the observation with the output of teh process model.
- trajectory generation 

#### Data driven approach
use trained ML model to make prediction of trajectories based on observed behaviors, it contains offline training and online prediction. Advantages are: use data to extract patterns that may be missed by model based approaches. Disadvantages are: purely depend on historical data and is black box.
steps:
- collection and clean trajectories
- define measures of similarity
- perform unsupervised clustering (agglomerative clustering or spectral clustering)
- define prototype trajectories for each cluster

- observe vehicle's partial trajectory
- compare to prototype trajectory (same similaritiy used in clusering)
- predict trajectory in each timestep

#### hybrid approach

- Intent classification
trajectory generation

- naive bayes


