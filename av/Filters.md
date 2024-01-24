## Kalman Filter
连续性预测的单一模型，由两步组成：
- state predict: addition based on total probability,
$$ μ^{'} \propto μ+\nu$$
$$(σ^2)^{'} = σ^2 + r^2$$
- measurement update: production based on bayes rule，
组合权重由方差决定。
$$ μ^{'} = \frac{r^2μ+σ^2\nu}{r^2+σ^2}$$
$$ (σ^2)^{'} = \frac{1}{\frac{1}{r^2}+\frac{1}{σ^2}}$$

### Design of KF
- state transition matrix
- measurement matrix


## Extended Kalman Filter
用于处理测量的非线性问题（比如Radar）。

## Particle Filter
