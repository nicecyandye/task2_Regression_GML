import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('data/train.csv')


X = df[['6']]
y = df['target']
X = X ** 2


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


predictions_val = model.predict(X_val)
rmse = mean_squared_error(y_val, predictions_val)
print(f'Validation RMSE: {rmse}')


joblib.dump(model, 'model/model.pkl')
