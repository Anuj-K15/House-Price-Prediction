import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

df = pd.read_csv('data/mumbai_house_price.csv')

def convert_price(row):
    if row['price_unit'] == 'Cr':
        return row['price'] * 100  
    return row['price']

df['price_in_lakhs'] = df.apply(convert_price, axis=1)

df.drop(['price', 'price_unit'], axis=1, inplace=True)

df['type'] = df['type'].astype('category').cat.codes
df['region'] = df['region'].astype('category').cat.codes

X = df[['bhk', 'type', 'area', 'region']]  
y = df['price_in_lakhs']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as model.pkl")
