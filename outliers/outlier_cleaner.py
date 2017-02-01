#!/usr/bin/python

import operator
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    #print type(predictions - net_worths)
    for i in range(len(predictions)):
        pred = predictions[i][0]
        age = ages[i][0]
        net_worth = net_worths[i][0]

        error = (net_worth - pred) ** 2
        cleaned_data.append((age, net_worth, error))

    # for pred, age, net_worth in zip(predictions, ages, net_worths):
    #     error = (net_worth - pred) ** 2
    #     cleaned_data.append((age, net_worth, error))

    #print cleaned_data
    cleaned_data = sorted(cleaned_data, key = operator.itemgetter(2))

    #print cleaned_data
    n = int(len(cleaned_data) * 0.9)

    return cleaned_data[0:n]

