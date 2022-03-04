import pandas as pd

data=pd.read_csv("sample_data/서울시 대기질 자료 제공_2020-2021.csv", encoding='utf-8')
df=pd.DataFrame(data)

head=df.head()
# print(head)

'''
Creating Columns
'''
df['month']=pd.to_datetime(df['일시'],format="%Y-%m-%d %H:%M").dt.month_name()
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# df['area']=df['width']*df['height']
head=df.head()
# print(head)

'''
Summary Statistics
'''
desc=df.describe()
# print(desc)

pm10=df['미세먼지(PM10)'].describe()
# print(pm10)

'''
Grouping
'''
num_month=df['month'].value_counts()
print(num_month,"\n")

total_mean=df['미세먼지(PM10)'].mean()
print(total_mean,"\n")

monthly_mean=df.groupby('month')['미세먼지(PM10)'].mean()
# calculating mean values of '미세먼지(PM10)' grouping by the diven col ('month')
print(monthly_mean,"\n")
