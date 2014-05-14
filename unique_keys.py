#This script was used to identify institutions for whom we had consecutive years of data, 
#i.e. a group with data from 2008 and 2007 would be returned but a group with 2009 and 2007 data would be skipped
#as the goal of this script was to identify which groups could be backfilled with the more recent year of information.

import csv

def read(filename):
    data = []
    with open(filename, 'rU') as f:
        f = csv.reader(f)
        for row in f:
            data.append(row)

    return data

def write(data, filename):
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# read file, remove headers
data = read('query_result.csv')
h = data.pop(0)

# indexes of the variables we're interested in
primary_key_index = 2
pub_year_index = 1

# create a list of only the primary keys
primary_keys = []
for row in data:
    primary_keys.append(row[primary_key_index])

# get unique primary keys by performing set, then convert to a list
unique_keys = list(set(primary_keys))

# this is where we'll save our data
to_print = []

# for each primary key...
for primary_key in unique_keys:

    # get all the rows of data that have this primary_key
    matches = []
    for row in data:
        if row[primary_key_index] == primary_key:
            matches.append(row)

    # only continue if we matched more than one row of data
    if len(matches) != 1:

        # sort the list of matches by year
        # reverse=True makes it sort descending
        desc = sorted(matches, key=lambda row: int(row[pub_year_index]), reverse=True)

        # enumerate is like a for loop, but it gives us both the index and the item in the list
        for index, value in enumerate(desc):

            # year_this is the current row of CSV data
            year_this = desc[index]
            # y1 is the actual year converted to int, ie 2009, 2010, etc.
            y1 = int(year_this[pub_year_index])

            # check if there's a year_next by comparing the current index + 1 with the length of the whole list
            # basically making sure we're not on the last item in the list
            if index + 1 < len(desc):

                # year_next is the row, y2 is the year
                year_next = desc[index+1]
                y2 = int(year_next[pub_year_index])

                # if the years are consecutive, add year_this to our list and continue (don't check year last)
                if y1 - y2 == 1:
                    to_print.append(year_this)
                    continue

            # check if there's a year_last by making sure index - 1 is not -1
            # basically making sure we're not on the first item in the list
            if index - 1 >= 0:

                year_last = desc[index-1]
                y3 = int(year_last[pub_year_index])

                # if the years are consecutive, add them to our output list
                # no need for a continue statement here, because it's the end of the loop
                if y1 - y3 == -1:
                    to_print.append(year_this)


write(to_print, 'output.csv')
