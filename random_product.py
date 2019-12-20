import pandas as pd
from random import randint
df = pd.read_csv('sort.csv')
price = df['price']
name = df['name']
img=df['img']
link=df['link']

def get_index(p_min,p_max):
    i_min=min([i for i in range(len(price)) if price[i]>=p_min])
    i_max=max([j for j in range(len(price)) if price[j]<=p_max])
    return i_min,i_max

def random(i,f):
    return randint(i,f)

def get_product(index): 
    # print(index)
    pd_name = name[index]
    pd_price = price[index]
    pd_img = img[index]
    pd_link = link[index]
    return pd_name,pd_price,pd_img,pd_link
    
lowest = int(input("Enter lowest price: "))
highest = int(input("Enter highest price: "))

i,f=get_index(lowest,highest)
index = random(i,f)
print(get_product(index))

