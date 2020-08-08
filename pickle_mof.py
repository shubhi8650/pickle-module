import pickle


#pickling

# cars = ['Audi','BMW','shubham']
#
# file = "mycar.pkl"
#
# fileObj = open(file, 'wb')
# pickle.dump(cars, fileObj )
# fileObj.close

#depickle

file = 'mycar.pkl'
fileObj = open(file, 'rb')
mycar = pickle.load(fileObj)
print(mycar)


