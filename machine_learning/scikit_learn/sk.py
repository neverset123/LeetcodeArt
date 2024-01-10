## linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y) # X必须是2d array，其中列为feature数
model.predict([ [127], [248] ])

## polynominal regression
from sklearn.preprocessing import PolynomialFeatures
poly_feat = PolynomialFeatures(degree = 4)
X_poly = poly_feat.fit_transform(X)
testing_data = poly_feat.transform(X_test)
poly_model = LinearRegression(fit_intercept = False).fit(X_poly, y)

## L1 regularization 
# lasso在线性回归损失函数基础上加入了L1正则化
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
lasso_reg = Lasso()
lasso_reg.fit(X_scaled, y)

## decision tree
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth = 7, min_samples_leaf = 10)
model.fit(X_train, y_train)
model.predict(X_test)

## naive bayes
from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)
predictions = naive_bayes.predict(testing_data)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(predictions, y_test)))
print('Precision score: ', format(precision_score(predictions, y_test)))
print('Recall score: ', format(recall_score(predictions, y_test)))
print('F1 score: ', format(f1_score(predictions, y_test)))

## SVM
from sklearn.svm import SVC
model = SVC(kernel='poly', degree=4, C=0.1)
model.fit(X, y)

## adaboost
from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier(base_estimator = DecisionTreeClassifier(max_depth=2), n_estimators = 4)
model.fit(x_train, y_train)
model.predict(x_test)

## classification metrics
from sklearn.model_selection import train_test_split
import numpy as np

X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=42)
accuracy = np.mean(preds == actual)

tp = len(np.intersect1d(np.where(preds==1), np.where(actual==1)))
pred_pos = (preds==1).sum()
prec = tp/(pred_pos)
act_pos = (actual==1).sum()
recall = tp/act_pos
f1 = 2*(prec*recall)/(prec+recall)

from sklearn.metrics import fbeta_score, f1_score, accuracy_score, precision_score, recall_score, roc_curve, auc, roc_auc_score
fbeta_score(y_test, preds_bag, beta=1)
f1_score(y_test, preds_bag)

fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(len(y_test)):
    fpr[i], tpr[i], _ = roc_curve(y_test, y_preds[:, 1])
    roc_auc[i] = auc(fpr[i], tpr[i])

## regression metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
error_abs = mean_absolute_error(y, y_pred)
error_squ = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

## validation
from sklearn.model_selection import KFold
kf = KFold(12,3,shuffle=True)
for train_indices, test_indices in kf:
    print(train_indices, test_indices)

## Learning Curves
from sklearn.model_selection import learning_curve
train_sizes, train_scores, test_scores = learning_curve(
    estimator, X, y, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, num_trainings))
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)

## grid search
from sklearn.model_selection import GridSearchCV
parameters = {'kernel':['poly', 'rbf'],'C':[0.1, 1, 10]}
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
scorer = make_scorer(f1_score)
grid_obj = GridSearchCV(model, parameters, scoring=scorer)
grid_fit = grid_obj.fit(X_train, y_train)
best_clf = grid_fit.best_estimator_
best_clf.fit(X_train, y_train)
best_train_predictions = best_clf.predict(X_train)
best_test_predictions = best_clf.predict(X_test)

##KMeans
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

clusters = 5
kmeans_cluster = KMeans(n_clusters=clusters, random_state=123)
df_ss = pd.DataFrame(StandardScaler().fit_transform(df), columns=[])
df_mm = pd.DataFrame(MinMaxScaler().fit_transform(df), columns=[])
kmeans_model = kmeans_cluster.fit(df_ss)
kmeans_prediction = kmeans_model.predict(df_ss)

## hierachical clustering
from sklearn import datasets, cluster
from scipy.cluster.hierarchy import dendrogram, ward, single
import matplotlib.pyplot as plt

clust = cluster.AgglomerativeClustering(n_clusters=3, linkage="ward")
labels = clust.fit_predict(X)

linkage_matrix = ward(X)
dendrogram(linkage_matrix)
plt.show()

## DBSCAN
from sklearn import datasets, cluster

db = cluster.DBSCAN(eps=0.5, min_samples=5)
db.fit(X)

## GMM
from sklearn import datasets, mixture

gmm = mixture.GaussianMixture(n_components=3, covariance_type="full", init_params="kmeans")
gmm.fit(X)
clustering = gmm.predict(X)

## ARI
from sklearn.metrics import adjusted_rand_score
score = adjusted_rand_score(pred, label)

## silhouette_score
from sklearn.metrics import silhouette_score
silhouette_avg = silhouette_score(X, cluster_label)

## PCA
from sklearn.decomposition import PCA

X = StandardScaler().fit_transform(data)
pca = PCA(n)
x_pca = pca.fit_transform(X)
num_components = len(pca.explained_variance_ratio_)
ind = np.arange(num_components)
vals = pca.explained_variance_ratio_
cumvals = np.cumsum(vals)
plt.plot(ind, cumvals)

mat_data = np.asmatrix(pca.components_[index]).reshape(28, 28)
plt.imshow(mat_data) #highlight important features

## random projection
# sklearn可以根据eps自动推算降维后的维度，eps越大，维度越低：也可以直接给定n_components参数
from sklearn import random_projection
rp = random_projection.SparseRandomProjection()
rp1 = random_projection.GaussianRandomProjection()
new_X = rp.fit_transform(X)

## ICA
from sklearn.decomposition import FastICA

X = list(zip(signal_1, signal_2, signal_3))
ica = FastICA(n_components=3)
components = ica.fit_transform(X)

