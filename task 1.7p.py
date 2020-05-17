'''7. Write a Pandas program to read a csv file from
 a specified source and print the first 5 rows'''

import pandas as pd

#in order to display all thae columns without squeezing

pd.set_option('display.max_columns', None)

sam_tab=pd.read_csv("https://github.com/RisabhKedai/Spectrum-internship-drive2020-TASK-1/raw/master/diamonds.csv",nrows=5)

print(sam_tab)
