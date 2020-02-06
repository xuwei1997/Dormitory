import pandas as pd


df=pd.read_excel('xs.xlsx')
# print(df)
df = df.sort_values(by='sID',ascending=False)
# print(df.sort_values(by='sID',ascending=False)) #降序
print(df[df.sClass==2].shape[0])#行数