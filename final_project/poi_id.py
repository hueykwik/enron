#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

features_list = ['poi', 'exercised_stock_options',
    'bonus', 'shared_receipt_with_poi', 'deferred_income', 'fraction_from_poi',
    'fraction_to_poi']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop("TOTAL", 0)
data_dict.pop("THE TRAVEL AGENCY IN THE PARK", 0)

### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator)
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """
    ### beware of "NaN" when there is no known email address (and so
    ### no filled email features), and integer division!
    ### in case of poi_messages or all_messages having "NaN" value, return 0.

    if poi_messages == "NaN" or all_messages == "NaN":
        return 0

    return poi_messages * 1.0 / all_messages

for name in data_dict:
    data_point = data_dict[name]

    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    data_point["fraction_from_poi"] = computeFraction(from_poi_to_this_person, to_messages)

    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    data_point["fraction_to_poi"] = computeFraction(from_this_person_to_poi, from_messages)


my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a variety of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
#from sklearn.naive_bayes import GaussianNB
#clf = GaussianNB()

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(random_state=42)

#from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier(random_state=42)

# # ### Task 5: Tune your classifier to achieve better than .3 precision and recall
# # ### using our testing script. Check the tester.py script in the final project
# # ### folder for details on the evaluation method, especially the test_classifier
# # ### function. Because of the small size of the dataset, the script uses
# # ### stratified shuffle split cross validation. For more info:
# # ### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# # # Example starting point. Try investigating other evaluation techniques!
# # from sklearn.cross_validation import train_test_split
# # features_train, features_test, labels_train, labels_test = \
# #     train_test_split(features, labels, test_size=0.3, random_state=42)

param_grid = {"criterion" : ["gini", "entropy"],
              "max_depth": [None, 1, 2],
              "min_samples_split": [2, 4, 8]
             }

from sklearn.model_selection import GridSearchCV, StratifiedShuffleSplit

clf = GridSearchCV(clf, param_grid, cv=StratifiedShuffleSplit(random_state=42))
clf.fit(features, labels)

print clf.best_params_
print clf.best_score_

clf = clf.best_estimator_
print clf
print clf.feature_importances_

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
