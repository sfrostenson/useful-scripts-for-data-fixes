# -*- coding: utf-8 -*-
import csv
#python module for regex
import re

#this function converts a csv file into a native python list.
#we must do this in order to alter the csv's contents.
#think of csvs as lists of lists.
def read(filename):
	data = []
	with open(filename, 'rU') as f:
		f = csv.reader(f)
		for row in f:
			data.append(row)
		return data

#this function removes both leading and trailing white spaces.
def rm_trails(s):
	return s.strip()

#the function below is an alternative to regular expressions.
#instead of establishing a pattern, you specify what string you want replaced instead.
# def replace_all(text, dic):
# 	# takes 2 arguments. text contains replacements. 
# 	#dic contains word or characters to be replaced as the key.
# 	#iteritems is a method to retrieve key & corresponding value from a dictionary.
# 	for i, j in dic.iteritems():
# 		text = text.replace(i, j)
# 	return text

#regex solution to find and replace
#always start with expression w/ r so you don't have to write a bajillion escapes
#^ specifies that we want to exclude everything EXCEPT the following, which is
#d= digit &. So in this instance, all currency/numbers preserved, everything else removed
#and replaced with nothing
#awesomesauce.
def numbers_only(s):
	#this is the regex equivalent of .replace()
	return re.sub(r'[^\d\.]', '', s)

#here i create a function to first convert my string to int  
#all csv content is read as strings by python unless specified
#if the string won't convert to int because it has a decimal and is a float
#try float instead when given Value Error and round to 0 decimal places.
#converts all numbers to either an int or rounded float.
def round_numbers(s):
	try:
		return int(s)
	except ValueError:
		try:
			return round(float(s), 0)
		except ValueError:
			return s

#call function read
rows = read('historical_edits.csv')
#remove headers to perform analysis; will add back on at end.
headers = rows.pop(0)
# for search and replace of words if using def replace_all
#in dictionaries, list words in a separate dictionary from characters
#can lead to unexpected find and replaces otherwise.
# w_reps = {'don\'t know' : '', 'n/a' : '', 'N/A' : ''}
# # for search and replace of characters
# c_reps = {',':'', '$':'', '< ':''}

#our list to append changes.
new_rows = []

for row in rows:
	# here we use the function rm_trails on the entire list.
	new_row = [rm_trails(x) for x in row]
	# here we say new_row instead of just row, b/c we are only specifying certain rows.
	new_row[11:17] = [numbers_only(x) for x in new_row[11:17]]
	new_row[11:17] = [round_numbers(x) for x in new_row[11:17]]
	new_row[19:21] = [numbers_only(x) for x in new_row[19:21]]
	new_row[42:53] = [numbers_only(x) for x in new_row[42:53]]
	new_row[59:63] = [numbers_only(x) for x in new_row[59:63]]
	new_row[66:69] = [numbers_only(x) for x in new_row[66:69]]
	new_row[19:21] = [round_numbers(x) for x in new_row[19:21]]
	new_row[42:53] = [round_numbers(x) for x in new_row[42:53]]
	new_row[59:63] = [round_numbers(x) for x in new_row[59:63]]
	new_row[66:69] = [round_numbers(x) for x in new_row[66:69]]

#append our work to the list new_rows
	new_rows.append(new_row)

#output file 
with open('output.csv', 'wb') as f:
  writer = csv.writer(f)
  writer.writerow(headers)
  writer.writerows(new_rows)
