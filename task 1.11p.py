'''11.  Write a Pandas program to count the duplicate rows of diamonds DataFrame.'''
import pandas as pd

imp_tab=pd.read_csv("https://github.com/RisabhKedai/Spectrum-internship-drive2020-TASK-1/raw/master/diamonds.csv")

lis=list(imp_tab.columns)

lis.remove('Sr No.')

print(lis)

print(imp_tab.duplicated(subset=lis,keep='first').sum())
