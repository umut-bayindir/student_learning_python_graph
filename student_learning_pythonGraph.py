import pandas as pd
import matplotlib.pyplot as plt


work_data = 'data.xlsx'

df = pd.read_excel(work_data)
print(df.head())

plt.title('Chart title')




first = df.plot.line(title='Chart title', x='Energy', y=['Spectrum', 'Background','peak1','peak2','peak3','fit'],figsize=(10,6),grid=True);


plt.show()