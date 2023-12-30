## linear regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y) # X必须是2d array，其中列为feature数
model.predict([ [127], [248] ])

## polynominal regression
from sklearn.preprocessing import PolynomialFeatures
poly_feat = PolynomialFeatures(degree = 4)
X_poly = poly_feat.fit_transform(X)
poly_model = LinearRegression(fit_intercept = False).fit(X_poly, y)

## regularization
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

## testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=42)
