from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import csv

a =[]
b= []

print("Stocks using Linear Regression\n")
def collect_data(filename):  #Function to read and save collected csv data
    rawdata = open(filename , 'r')
    data = csv.reader(rawdata)
    next(data)
    for row in data:
        a.append(int(row[0]))
        b.append(float(row[1]))

def plot_predict_model(a,b, x):  #Function to plot our model and predict
    model = linear_model.LinearRegression()
    returns = np.reshape(a,(len(a),1))
    dividend = np.reshape(b,(len(b),1))
    model.fit(returns,dividend)
    plt.scatter(returns, dividend, color='cyan')  #Plot of the collected data on the coordinates
    plt.plot(returns, model.predict(returns), color='red', linewidth=5)  # Plot of the line (model fit) formed by Linear Regreesion
    plt.show()
    predicted_divedend = model.predict(x)  #Predicting the stock open price on Sep. 29th
    coef = model.coef_[0][0]  #Coefficient(m) of the model formed (Y = m*X + c)
    intercept = model.intercept_[0]  #Intercept(c) of the model formed (Y = m*X + c)
    print("Predicted dividend for stock is: ",predicted_divedend[0][0])
    print("The coefficient and intercept of the formed model by Linear Regression are: ", coef , intercept )

collect_data('sample_stocks.csv')
plot_predict_model(a,b,1)