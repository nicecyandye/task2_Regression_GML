import pandas as pd
import joblib


model = joblib.load('model/model.pkl')
test_data = pd.read_csv('data/hidden_test.csv')

# Pre-processing
test_data = test_data[['6']]
test_data = test_data ** 2

predictions = model.predict(test_data)

pd.DataFrame(predictions, columns=['predictions']).to_csv('data/predictions.csv', index=False)
