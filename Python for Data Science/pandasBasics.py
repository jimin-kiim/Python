"""
Pandas : derived from the term "panel data", 
        an econometrics term for data sets that include observations over multiple time periods for the same individuals.
Series : essentially a column (one dimensional array). A series is like a DataFrame, but it's just a single column.

DataFrame : a multi-dimensional table made up of a collection of Series.

"""

import pandas as pd

'''
pd.options.display.max_columns = num

DataFrame : automatically creates a numeric index for each row. 
            can be specified, when being created.

accessing row : df[{condition}]
                df.loc[""], df.loc[["","",""]]
                df.iloc[i]
                df.head()
                df.tail()
accessing col : df[""], df[["","",""]]; using list inside the square brackets.

setting our own index column : df.set_index("", inplace=True)
                                inplace=True :
                                the change will be applied to our DataFrame,
                                without the need to assign it to a new DataFrame variable.
info : df.info()
        df.shape

deleting row : df.drop("",axis=0, inplace=True)
deleting col : df.drop("",axis=1, inplace=True)

creating col : df['']=~~~

statistics : 
        summarty : df.describe()
        sum : df[''].sum()
        mean : df[''].mean()
        max : df[''].max()
        min : df[''].min()

Series.values -> convert data in a Pandas DataFrame to a numpy array(1-dimensional array)
DataFrame.values -> convert data in a Pandas DataFrame to a numpy array(2-dimensional array)
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

print("first two rows \n",df.head(2),"\n")
# getting the first rows of the data. 
# default : first 5 rows. 
print("last two rows\n", df.tail(2),"\n")

print(df.info(),"\n")

age_mean=df['ages'].mean()
print(age_mean)

'''
Grouping 

frequency of the values : df[""].value_counts()

df.groupby('grouping_col')['value_col'].mean()
'''