import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    "size": [500, 700, 900, 1100, 1300, 1500, 1700, 2000],
    "price": [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 5000000]
}

df = pd.DataFrame(data)

X = df[['size']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained & saved")