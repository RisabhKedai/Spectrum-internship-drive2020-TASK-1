'''8. Write a Pandas program to select a series from diamonds DataFrame. 
Print the content of the series.'''
import pandas as pd
imp_tab=pd.read_csv("C:/Users/Lenovo/Desktop/diamonds.csv")
print("Select a series from below ")
#printing a list of columns
print(imp_tab.columns)
s=input("enter the name \n")
g=input("enter the number of rows you want to display. enter q for squeezed view\n")
print("these are the values for the series")
if g=='q':
    print(imp_tab[s])
else:
    print(imp_tab[s].head(int(g))) 
    