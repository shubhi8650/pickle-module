import requests
import pickle

#this link is from IRIS DATASET FROM  machine learning

r  = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data').text


l1 = r.split('\n')
# print(l1)

l2 = [item.split(',') for item in l1 if len(item)!= 0]


file = 'ex10.pkl'

fileObj = open(file, 'wb')

# pickle.dump(l2,fileObj)


# #to read this pickle file we can use the below code
#
# import pickle
# with open('ex10.pkl', 'rb') as f:
#     print(pickle.load(f))


