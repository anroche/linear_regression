import sys
import csv
import re

import numpy as np
import matplotlib.pyplot as plt

learningRate = float(0.001)
maxIter = 50000
precision = 2

def plot_data(theta0, theta1, km, price):
    plt.plot([predict_price(theta0, theta1, x) for x in range(250000)], "b", linewidth=3)
    plt.plot(km, price, "ro")
    plt.show()

def predict_price(theta0, theta1, km):
	estimate_price = theta0 + theta1 * km
	return estimate_price

def cost_error(theta0, theta1, X, Y):
	error = 0
	m = len(X)
	for i in range(len(X)):
		error += (Y[i] - predict_price(theta0, theta1, Y[i])) **2
	error = 1/2/m * error
	return error

def average(lst): 
    return sum(lst) / len(lst) 

def multiply_list(lista, listb):
	ret = [a*b for a,b in zip(lista,listb)]
	return ret

def open_data():
	km = []
	price = []
	try:
		with open(sys.argv[1]) as (csv_file):
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				try:
					km.append(float(row[0]))
					price.append(float(row[1]))
				except:
					print("")
		return (km, price)
	except:
		print("Data invalid")
		exit()

def save_theta(theta0, theta1):
		filetheta = open("theta.csv", 'w+')
		filetheta.write(str(theta0) + "," + str(theta1))
		filetheta.close()
	 
def norm_data(X, Y):
	maxX = max(X)
	maxY = max(Y)
	normX, normY = [], []
	for i in range(len(X)):
		normX.append(X[i]/maxX)
		normY.append(Y[i]/maxY)
	return (normX, normY)

def sigma(theta0, theta1, X, Y):
	tmp0 = 0.0
	tmp1 = 0.0
	i = 0
	m = len(X)
	gap = 1
	while (i < m and gap < precision):
		tmp0 += (predict_price(theta0, theta1, X[i]) - Y[i])
		tmp1 += ((predict_price(theta0, theta1, X[i]) - Y[i]) * X[i])
		gap = tmp0 - theta0
		gap = abs(gap)
		i += 1
	t0 = theta0 - learningRate * ((1.0/float(m)) * tmp0)
	t1 = theta1 - learningRate * ((1.0/float(m)) * tmp1)
	return (t0, t1)

def linear_regression(X, Y):
    theta0 = 0.0
    theta1 = 0.0
    for i in range(maxIter):
        theta0, theta1 = sigma(theta0, theta1, X, Y)
    return(theta0, theta1)

def print_regression(X, Y, theta0, theta1):
	axes = plt.axes()
	axes.grid()
	plt.ylabel("Prices")
	plt.xlabel("kilometres")
	plt.xlim()

	x = np.linspace(0,max(X) * 1.5,100)
	y = theta1*x+theta0	
	plt.plot(X, Y, "xb",  label='Data set') 
	plt.plot(x, y, '-r', label='Linear regression')
	plt.legend(loc='upper left')
	plt.show()


def main(): 

    X, Y = open_data()
    normX, normY = norm_data(X, Y)
    theta0, theta1 = linear_regression(normX, normY)  
    theta0 = theta0 * max(Y)
    theta1 = (theta1 * max(Y)) / max(X)
    print_regression(X, Y, theta0, theta1)
    save_theta(theta0, theta1)
	
if __name__ == "__main__":
    main()