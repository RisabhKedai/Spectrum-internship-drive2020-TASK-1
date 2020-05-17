'''9. Write a Pandas program to calculate 
count, minimum, maximum price for each cut of diamonds DataFrame'''
import pandas as pd
imp_tab=pd.read_csv("C:/Users/Lenovo/Desktop/diamonds.csv")

#first grouping by different types of cuts
a=imp_tab.groupby('cut')
#agg() used to aggregate various functions to be applied on a column
k=a.price.agg(['count','min','max']).rename(columns={'count':'price count','max':'maximum price','min':'minimum price'})
print(k)

