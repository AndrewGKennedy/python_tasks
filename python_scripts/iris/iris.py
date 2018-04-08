#Author: Andrew Kennedy GOO364899
#Problem, read in Iris csv file, format nd print to screen in a nice format
#Date 08/04/2018 
#Version 1.0
#Release 1

#Ref:https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
#Ref: https://archive.ics.uci.edu/ml/datasets/Iris/

#import numpy - numeric package
#import csv utilities
import numpy as np
import csv

#pip install tabulate module first
from tabulate import tabulate

#Define array for header
header = ['Petal Length', 'Petal Width', 'Sepan Lenght', 'Sepal Width', 'Name']
#use open routine as we will not havd to worry about close
iris = open('data\iris.csv')

#array used to store lines read in
data_array = []

#open the file
with open('data\iris.csv')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
            data_array.append(row)
            table = tabulate(data_array, headers=header,numalign="right",stralign='left')
print(table)
