'''10. Write a Pandas program to check the number of rows and columns and drop those row
 if "any" values are missing in a row of diamonds DataFrame.'''
import pandas as pd

imp_tab=pd.read_csv("https://github.com/RisabhKedai/Spectrum-internship-drive2020-TASK-1/raw/master/diamonds.csv")

print("the number of rows and columns are")

print("Rows:%d Columns:%d"%(imp_tab.shape))

#drop the dublicate rows

lis=list(imp_tab.columns)

lis.remove('Sr No.')

# lis has all column names except Sr No. because every row has to have a different serial no.

imp_tab.dropna(axis=0,thresh=None,how='any',subset=lis)

print('after deleting the duplicate rows')

print("Rows:%d  Columns:%d"%(imp_tab.shape))
