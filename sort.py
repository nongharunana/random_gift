import pandas as pd
df = pd.read_csv('products.csv')
re=df.sort_values('price')
export_csv = re.to_csv (r'sort.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path
