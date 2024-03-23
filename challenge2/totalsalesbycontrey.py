import pandas as pd
import matplotlib.pyplot as plt


df_users = pd.read_csv('AIQ - Management Trainee Assignment - Challenge_2_users.csv')

df_orders = pd.read_csv('AIQ - Management Trainee Assignment - Challenge_2_orders.csv')

df_merged = df_orders.merge(df_users[['id', 'country']], how='left', left_on='user_id', right_on='id')

df_country_sales = df_merged.groupby('country')['value'].sum()

df_table = pd.DataFrame({'Country of Origin': df_country_sales.index, 'Total Sales': df_country_sales.values})
print(df_table.to_string(index=False))

df_country_sales = df_country_sales.sort_values(ascending=False)

plt.figure(figsize=(10, 5))  
plt.bar(df_country_sales.index, df_country_sales.values)
plt.xlabel('Country of Origin')
plt.ylabel('Total Sales')
plt.title('Total Sales by Country (Highest First)')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()  
plt.savefig('total_sales_by_country.png')  

