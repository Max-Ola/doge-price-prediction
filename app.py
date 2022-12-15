import pandas as pd
from sklearn.linear_model import LinearRegression
from django.http import HttpResponse
from django.shortcuts import render

# Load the historical Dogecoin data into a Pandas DataFrame
df = pd.read_csv('dogecoin_data.csv')

# Train a Linear Regression model on the data
model = LinearRegression()
X = df[['time', 'market_conditions']]
y = df['price']
model.fit(X, y)

def dogecoin_prediction(request):
    # Get the user-specified time period and market conditions from the request
    time = request.GET['time']
    market_conditions = request.GET['market_conditions']

    # Use the trained model to predict the Dogecoin price
    prediction = model.predict([[time, market_conditions]])

    # Render a template with the prediction result
    return render(request, 'dogecoin_prediction.html', {'prediction': prediction})
