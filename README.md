useful-scripts-for-data-fixes
=============================

Python scripts for data fixes. As of 03.20.13 contents include:

(1) **skipblanks.py**: script that says if value in field of spreadsheet/csv is blank, skip and only write fields with                           content into new file.

(2) **tranpose_all.py**: script that uses the iterator module to do a souped up version of zip (izip) that will transpose                          all rows of data into "columns" in your new file. I put "columns" in quotes b/c python doesn't 
                         natively read columns--what we're doing here is reorganizing values w/i a matrix essentially.

(3) **transpose_some.py**: script that parses specified x rows of data (not all) into x columns (each specification = 1                              column) and in this instance, also fills additional corresponding columns with specified data.

(4) **blanks.py**: script that runs a for loop that fills blank fields in a row with the last row's value. in this 
                   instance, I am filling to rows with last row information.
