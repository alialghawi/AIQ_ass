import pandas as pd
import matplotlib.pyplot as plt

filepath = 'AIQ - Management Trainee Assignment - Challenge_2_orders.csv'
df_orders = pd.read_csv(filepath)

df_orders['timestamp'] = pd.to_datetime(df_orders['timestamp'], format='%Y-%m-%d %H:%M:%S') 

df_orders.set_index('timestamp', inplace=True)

df_monthly_sales = df_orders.resample('M')['value'].sum()

df_monthly_sales.plot(kind='line')
plt.xlabel('Month')
plt.ylabel('Cumulative Sales')
plt.title('Monthly Cumulative Sales')
plt.savefig('cumulativesalesgraph.png')  
