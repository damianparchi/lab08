import numpy as np
import pandas as pd
import xlrd
import openpyxl


df=pd.read_csv('zamowienia.csv', sep=';')

#print(df.Sprzedawca.unique())
#df2=df.nlargest(5, ['Utarg'])
#print(df2.Utarg)


#print(df.groupby(df['Sprzedawca']).agg({'idZamowienia':['count']}))

#print(df.groupby(df.Kraj).agg({'idZamowienia':['count']}))

#print(df.groupby(df.Kraj=='Polska').agg({'idZamowienia':['count']}))
#print(df.groupby(df['Kraj']).agg({'idZamowienia':['count']}))

#print(df.loc[((df['Kraj']=='Polska')&(df['Data zamowienia']<'2006-01-01')) & (df['Data zamowienia']>'2004-12-31'), 'idZamowienia'].sum())

#print(df.loc[((df['Data zamowienia']<'2005-01-01')) & (df['Data zamowienia']>'2003-12-31'), 'Utarg'].mean())

dane1 = df.loc[((df['Data zamowienia']<'2005-01-01')) & (df['Data zamowienia']>'2003-12-31')]
dane2 = df.loc[((df['Data zamowienia']<'2006-01-01')) & (df['Data zamowienia']>'2004-12-31')]
dane1.to_csv('zamowienia_2004.csv')
dane2.to_csv('zamowienia_2005.csv')