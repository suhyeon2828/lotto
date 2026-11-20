import pandas as pd

df = pd.read_csv('lotto.csv',encoding='utf-8-sig')
print(df.shape)
print(df.head(3))
print(df['당첨번호1'].head(5).tolist())