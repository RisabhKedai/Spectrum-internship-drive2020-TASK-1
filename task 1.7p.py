'''7. Write a Pandas program to read a csv file from
 a specified source and print the first 5 rows'''

import pandas as pd

pd.set_option('display.max_columns', None)

sam_tab=pd.read_csv("C:/Users/Lenovo/Desktop/diamonds.csv",nrows=5)

print(sam_tab)