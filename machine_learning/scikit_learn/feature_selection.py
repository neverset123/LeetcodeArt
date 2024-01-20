## 完全删除缺少大量数据的列和行
## Isolation forest剔除outlier
from sklearn.ensemble import IsolationForest
clf = IsolationForest(random_state=0).fit(X)
pred = clf.predict([[0, 0], [10, 10]])

## 去除低方差特征(高相关性特征)
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)

## 单变量特征选择，去除低p值特征（低相关性特征）
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
selector = SelectKBest(chi2, k=len(X)) #score function: chi2, f_classif, mutual_info_classif（分类），f_regression, mutual_info_regression（回归）
selector.fit(X, y)
scores = -np.log10(selector.pvalues_) #特征重要性，可以根据排序选择前几个特征

## 递归特征消除, 递归特征消除法使用一个基模型来进行多轮训练，每轮训练后，消除若干权值系数的特征，再基于新的特征集进行下一轮训练
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
selector = RFE(estimator=SVC(kernel="linear", C=1), n_features_to_select=1, step=1).fit(X, y)
print(selector.ranking_) #特征重要性，可以根据排序选择前几个特征

## 基于模型的特征选择
from sklearn.feature_selection import SelectFromModel
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression, RandomizedLogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False)
lr = LogisticRegression(C=0.01, penalty="l1", dual=False)
rlr = RandomizedLogisticRegression(C=0.01, penalty="l1", dual=False)
etc = ExtraTreesClassifier()
selector = SelectFromModel(estimator=lsvc).fit(X, y)
print(selector.estimator_.coef_) #特征重要性，可以根据排序选择前几个特征
print(selector.threshold_) #阈值
print(selector.get_support()) #选择的特征
selector.transform(X)  #特征提取结果

## 去除共线性特征, VIF（方差膨胀因子）, VIF越大说明该变量越多的解释了其他变量的变异，VIF值大于10的变量存在共线性
from statsmodels.stats.outliers_influence import variance_inflation_factor
df = pd.DataFrame()
df["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
df["features"] = X.columns
df.sort_values(by='VIF Factor', ascending=False)

## PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_) #特征重要性，可以根据排序选择前几个特征
print(pca.singular_values_) #奇异值
print(pca.components_) #主成分


