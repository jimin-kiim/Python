import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("Python for Data Science/sample_data/서울시 대기질 자료 제공_2020-2021.csv", encoding='utf-8')
df=pd.DataFrame(data)

df['month']=pd.to_datetime(df['일시'],format="%Y-%m-%d %H:%M").dt.month_name()


df[df['month']=='May']["미세먼지(PM10)"].plot(kind="box")
plt.savefig('Python for Data Science/result_img/pm10_may_box.png')
# https://en.wikipedia.org/wiki/Box_plot