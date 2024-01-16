## 完全删除缺少大量数据的列和行
## Isolation forest剔除outlier
from sklearn.ensemble import IsolationForest
clf = IsolationForest(random_state=0).fit(X)
pred = clf.predict([[0, 0], [10, 10]])
