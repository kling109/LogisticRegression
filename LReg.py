import math

NUM_ATTRIBUTES = 2
TRAIN_DATA_FILE = "reg_train.csv"


#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
	data = []
	x = []
	y = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		x.append(float(instance[0].strip()))
		y.append(float(instance[1].strip()))

	f.close()
	data.append(x)
	data.append(y)
	return data


def printParams(params):
	print("The value of B0 (intercept) is: ", params[0])
	print("The value of B1 (slope) is: ", params[1])


#The linear regression algorithm. Takes a list of lists as input
def lreg(ind_variable,dep_variable):
	params = []
	B0 = 0.0
	B1 = 0.0

    #estimate the linear regression parameters (B0 and B1) here
	N = int(len(ind_variable))
	x_bar = sum(ind_variable)/N
	y_bar = sum(dep_variable)/N
	numer = sum([(ind_variable[i] - x_bar)*(dep_variable[i] - y_bar)
	             for i in range(N)])
	denom = sum([(ind_variable[i] - x_bar)**2 for i in range(N)])
	B1 = numer/denom
	B0 = y_bar - B1 * x_bar
	params.append(B0)
	params.append(B1)
	return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	parameters = lreg(train_matrix[0],train_matrix[1])
	printParams(parameters)
