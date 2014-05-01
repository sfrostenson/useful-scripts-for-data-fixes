useful-scripts-for-data-fixes
=============================

.py scripts for data fixes. As of 05.01.14 contents include:

(1) **fillblanks.py**: script that runs a for loop that fills blank fields in a row with the last row's value. in this 	instance, I am filling rows with last row information.
                   
(2) **skipblanks.py**: script that says if value in field of spreadsheet/csv is blank, skip and only write fields with   content into new file.

(3) **tranpose_all.py**: script that uses the iterator module to do a souped up version of zip (izip) that will transpose all rows of data into "columns" in your new file. I put "columns" in quotes b/c python doesn't natively read columns--what we're doing here is reorganizing values w/i a matrix essentially.

(4) **transpose_some.py**: script that parses specified x rows of data (not all) into x columns (each specification = 1  column) and in this instance, also fills additional corresponding columns with specified data.

(5) **clean_numbers.py**: script that looks at numeric data--in my case--currency, and removes characters that are not part of an integer or a float. Additionally, I round the float numbers. 


