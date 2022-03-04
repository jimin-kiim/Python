'''
Reading Data

pd.read_csv("")
        CSV(comma-separated values)
'''
import pandas as pd

data=pd.read_csv("Python with BeautifulSoup/jobs.csv")
df=pd.DataFrame(data)

head=df.head()
# print("""==============================
# first five rows
# ==============================
# """,head,"\n")

tail=df.tail()
# print("""==============================
# last five rows
# ==============================
# """,tail,"\n")

info=df.info()
# print(info,"\n")

df.set_index("title",inplace=True)
# print(df.head())

df.drop("link",axis=1,inplace=True)
# print(df.head())
df.drop("H1B Processing For Niche IT Professionals",axis=0,inplace=True)
print(df.head())

