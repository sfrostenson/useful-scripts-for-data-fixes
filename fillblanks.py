import csv

# read file
f = open('progareas2013.csv', 'rU')
reader = csv.reader(f)

# save file data as native python list
# (just easier working with csv's this way)
data = []
for row in reader:
    data.append(row)

# close file
f.close()

# last row variable
last_row = []

for row in data:

    # check to see if there's external id
    if row[0] is '':
        # if it's blank, fill in using last year
        row[0] = last_row[0]
        row[1] = last_row[1]

    # always save the current row for the next iteration
    # this way we're always back-filling with the right data
    last_row = row

# output
o = open('progareas2013_new.csv', 'wb')
writer = csv.writer(o)
writer.writerows(data)
