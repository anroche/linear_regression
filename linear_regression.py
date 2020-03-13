import sys
import csv
import re


import numpy as np
import matplotlib.pyplot as plt

def average(lst): 
    return sum(lst) / len(lst) 

def multiply_list(lista, listb):
	ret = [a*b for a,b in zip(lista,listb)]
	return ret

def visualization(km, price):
	plt.title("visualizor") 
	plt.xlabel("x") 
	plt.ylabel("y")
	axes.grid()
	plt.plot(km, price, "xr") 
	plt.show()

def open_data():
	km = []
	price = []
	try:
		with open(sys.argv[1]) as (csv_file):
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
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

def estimate_coef(km, price):

	nb_point = len(km)
	m_km = average(km)
	m_price = average(price)
	
	km_price = multiply_list(km, price)
	km_km = multiply_list(km, km)

	SS_xy =  sum(km_price) - nb_point * m_price * m_km
	SS_xx =  sum(km_km) - nb_point * m_km * m_km

	b_1 = SS_xy / SS_xx
	b_0 = m_price - b_1 * m_km
	
	return(b_0, b_1)


def save_theta(theta0, theta1):
		filetheta = open("theta.csv", 'w+')
		filetheta.write(str(theta0) + "," + str(theta1))
		filetheta.close()

def print_regression(km, price, theta0, theta1):
	axes = plt.axes()
	axes.grid()
	plt.ylabel("Prices")
	plt.xlabel("kilometres")
	plt.xlim()

	x = np.linspace(0,max(km) * 1.5,100)
	y = theta1*x+theta0	
	plt.plot(km, price, "xb",  label='Data set') 
	plt.plot(x, y, '-r', label='Linear regression')
	plt.legend(loc='upper left')
	plt.show()


def main(): 

	km, price = open_data()
	
	theta0 = 0
	theta1 = 0
	
	theta0, theta1 = estimate_coef(km, price)
	print_regression(km, price, theta0, theta1)
	#test()
	save_theta(theta0, theta1)
	

if __name__ == "__main__":
    main() 



