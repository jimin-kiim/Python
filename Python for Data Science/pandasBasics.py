"""
Pandas : derived from the term "panel data", 
        an econometrics term for data sets that include observations over multiple time periods for the same individuals.
Series : essentially a column (one dimensional array)
DataFrame : a multi-dimensional table made up of a collection of Series.

"""

import pandas as pd

'''
DataFrame : automatically creates a numeric index for each row. 
            can be specified, when being created.
            accessing row : df.loc[""], df.loc[["","",""]]
                            df.iloc[i]
            accessing column : df[""], df[["","",""]]
'''
data= {'ages':[14, 20, 34, 56], 'height': [145, 163, 180, 172]}

df=pd.DataFrame(data)
print(df,"\n")

df=pd.DataFrame(data, index=['A','B','C','D'])
print(df,"\n")
print(df.loc['A'],"\n")
print(df.loc[["A","C"]],"\n")
print(df["ages"],"\n")
print(df[["ages","height"]],"\n")

print(df.iloc[2],"\n")
print(df.iloc[1:3],"\n")
print(df.iloc[-2:],"\n")

print(df[ (df['ages'] < 40) & (df["height"]>150)],"\n")
print(df[ (df['ages'] < 30) | (df["height"]==180)],"\n")
