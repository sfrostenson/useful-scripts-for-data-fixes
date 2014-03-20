import csv
#uses a souped up verson of zip in the itertools which is a module for creating quick, efficient iterations in python
from itertools import izip
#set our variable a, and open our csv with the izip function that converts rows to columns
a = izip(*csv.reader(open('OUTPUT2.csv', 'rU')))
#the csv writer opens our new file, names it and writes the rows from a transposed so that now our rows are columns.
csv.writer(open('TRANSPOSE.csv', 'wb')).writerows(a)
