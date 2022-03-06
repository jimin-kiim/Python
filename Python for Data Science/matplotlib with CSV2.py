import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("Python for Data Science/sample_data/서울시 대기질 자료 제공_2020-2021.csv", encoding='utf-8')
df=pd.DataFrame(data)

df['month']=pd.to_datetime(df['일시'],format="%Y-%m-%d %H:%M").dt.month_name()

df[df['month']=='May']["미세먼지(PM10)"].plot(kind="box")
plt.savefig('Python for Data Science/result_img/pm10_may_box.png')
# https://en.wikipedia.org/wiki/Box_plot

df[df['month']=='May']["미세먼지(PM10)"].plot(kind="hist")
plt.savefig('Python for Data Science/result_img/pm10_may_hist.png')

(df[df['month']=='March'])[['미세먼지(PM10)','초미세먼지(PM25)']].plot(kind="area",stacked=False)
plt.savefig('Python for Data Science/result_img/pm10_mar_area.png')

(df[df['month']=='March'])[['미세먼지(PM10)','초미세먼지(PM25)']].plot(kind="scatter",x='미세먼지(PM10)',y='초미세먼지(PM25)')
plt.savefig('Python for Data Science/result_img/pm10_mar_scatter.png')
# A scatter plot is used to show the relationship between two variables.

df.groupby('month')['미세먼지(PM10)'].sum().plot(kind="pie")
plt.savefig('Python for Data Science/result_img/monthly_pm10_sum.png')
# Pie charts are usually used when you have up to 6 categories.