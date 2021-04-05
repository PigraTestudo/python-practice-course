import pandas as pd
import requests as req

url = 'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx'
req_g = req.get(url).content
df = pd.ExcelFile(req_g).parse()

df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])
print(df_sorted)
