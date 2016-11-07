#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def showOutliers(data_dict, features):
    features.pop(0)
    data = featureFormat(data_dict, features)
    for point in data:
        salary = point[0]
        bonus = point[1]
        matplotlib.pyplot.scatter( salary, bonus )

    matplotlib.pyplot.xlabel(features[0])
    matplotlib.pyplot.ylabel(features[1])
    matplotlib.pyplot.show()
