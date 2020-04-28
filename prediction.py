import sys
import csv
import re

def predict_price(theta0, theta1, X):
	estimate_price = theta0 + theta1 * X
	return estimate_price

def open_data():
	with open('theta.csv') as (csv_file):
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = next(csv_reader)
		theta0 = float(row[0])
		theta1 = float(row[1])
	return (theta0, theta1)		

def	main():
	print ('Veuillez indiquer le nombre de kilometre : ')
	X = float(input())

	try:
		theta0, theta1 = open_data()
	except:
		theta0 = 0
		theta1 = 0

	estimate_price = predict_price(theta0, theta1, X)
	print ('approximate price :', estimate_price)

if	__name__ == '__main__':
	main()