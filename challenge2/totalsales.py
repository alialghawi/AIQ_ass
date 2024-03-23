import pandas as pd
import matplotlib.pyplot as plt

filepath = 'AIQ - Management Trainee Assignment - Challenge_2_orders.csv'
df_orders = pd.read_csv(filepath)

df_orders['timestamp'] = pd.to_datetime(df_orders['timestamp'], format='%Y-%m-%d %H:%M:%S') 

df_filtered = df_orders.loc[(df_orders['timestamp'].dt.year == 2023) & (df_orders['timestamp'].dt.month == 12)]

total_sales_december = df_filtered['value'].sum()

print("Total sales in December 2023:", total_sales_december)
