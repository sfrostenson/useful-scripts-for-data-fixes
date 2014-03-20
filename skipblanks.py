import csv

# read file
f = open('progareas_2014.csv', 'rU')
reader = csv.reader(f)

# make a list to append content list to so we have a list that captures every row and not one row.
data_to_write = []
for row in reader:
	#content = list, which acts as template to append to data_to_write, which captures all rows.
  content = []
  for field in row:
    # this will be true if it's not empty and will append. if empty, skip.
    if field: 
    	content.append(field)
  data_to_write.append(content)
      

# output
o = open('OUTPUT.csv', 'wb')
writer = csv.writer(o)
writer.writerows(data_to_write)
