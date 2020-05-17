'''12. Write a Pandas program to get sample 75% of the diamonds DataFrame's rows 
without replacement and store the remaining 25% of the rows in another DataFrame'''

import pandas as pd

imp_tab=pd.read_csv("https://github.com/RisabhKedai/Spectrum-internship-drive2020-TASK-1/raw/master/diamonds.csv")

samp=imp_tab.sample(frac=0.75,replace=False,axis=0)

print("the 75% sample of the dataframe:-")
print(samp)

'''reat 25% of the dataframe assigned to rest 25'''
rest25=imp_tab[~imp_tab.index.isin(samp.index)]

print('Rest 25% of the dataframe:-')
print(rest25)
