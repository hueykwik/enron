#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print type(enron_data)

# print len(enron_data)

#pois = [k for k,v in enron_data.items() if v["poi"] == True]
#print len(pois)

#for k, v in enron_data.items():
#     print v["poi"]


print enron_data

# names = ["LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"]

# max_total = None
# max_name = None
# for name in names:
#     total = enron_data[name]["total_payments"]
#     if max_total is None or total > max_total:
#         max_total = total
#         max_name = name

# print max_name, max_total

#print enron_data["SKILLING JEFFREY K"]
