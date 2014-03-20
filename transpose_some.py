import csv
f = open('OUTPUT2.csv', 'rU')
reader = csv.reader(f)

#create list to append to
output_rows = []

for row in reader:
	#this tells the script to look at values in rows starting in position 2 onwards
	for prog_id in row[2:]:
		#skip row if blank
		if prog_id is '':
			pass
		#not blank? append postion [0], string '2014', postion [1] + prog_id, which is row 2 onward as individual rows
		#we are parsing the prog_ids into individual rows in one column with the stuff before prog_id repeating in ea. instance.
		else:
			output_rows.append([row[0], '2014', row[1], prog_id])

#write new file
o = open('fmreplicate.csv', 'wb')
writer = csv.writer(o)
writer.writerows(output_rows)

# close file
f.close() 
o.close()
