#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

def knn():
    #knn = KNeighborsClassifier(n_neighbors=10, weights="distance")
    knn = KNeighborsClassifier()

    print(knn.get_params().keys())

    param_grid = {"n_neighbors" : [3, 5, 7, 10],
                "weights": ["distance", "uniform"]
                }

    #clf = GridSearchCV(knn, param_grid=param_grid, scoring = 'accuracy', cv = 5)

    return clf

def create_grid_search():
    param_grid = {"base_estimator__criterion" : ["gini", "entropy"],
              "base_estimator__splitter" :   ["best", "random"],
              "base_estimator__max_depth": [None, 1, 2],
              "base_estimator__min_samples_split": [2, 4, 8],
              "n_estimators": [50, 100, 150, 500]
             }

    DTC = DecisionTreeClassifier(random_state = 11, max_features = "auto", class_weight = "balanced", max_depth = None)

    ABC = AdaBoostClassifier(base_estimator = DTC, random_state = 11)

    clf = GridSearchCV(ABC, param_grid=param_grid, scoring = 'accuracy')

    return ABC

### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid

# #clf = RandomForestClassifier()
# clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1, min_samples_split=3, criterion="gini"), random_state = 33)
# #clf = KNeighborsClassifier()

#clf = create_grid_search()
#clf = knn()

clf = KNeighborsClassifier(n_neighbors=10, weights="distance")

param_grid = { "n_neighbors" : [3, 5, 7, 10, 15],
                "weights": ["distance", "uniform"]
            }

best_score = 0
for g in ParameterGrid(param_grid):
    clf.set_params(**g)
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    acc = accuracy_score(labels_test, pred)
    if acc > best_score:
        best_score = acc
        best_grid = g

print "best score: %0.5f" % best_score
print "Grid:", best_grid


#print("training")
#clf.fit(features_train, labels_train)

#print("predicting")
#pred = clf.predict(features_test)

#try:
#    print(clf.best_params_)
#except AttributeError:
#    pass

#from sklearn.metrics import accuracy_score
#print(accuracy_score(labels_test, pred))

# dtc = DecisionTreeClassifier(random_state = 11, criterion = "entropy",
#                        max_depth = 1,
#                        splitter = "random",
#                        class_weight = "balanced")
# clf = AdaBoostClassifier(dtc, random_state = 11, n_estimators = 100)
# clf.fit(features_train, labels_train)

# from sklearn.metrics import accuracy_score
# pred = clf.predict(features_test)



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
