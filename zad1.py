  
import numpy as np
import pandas as pd
import xlrd
import openpyxl


x=pd.ExcelFile('imiona.xlsx')
df=pd.read_excel(x, 'Arkusz1')
print(df)