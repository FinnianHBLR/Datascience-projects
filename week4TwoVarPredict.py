import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error

def myCode():
    # Needs to reshape to be a 2D array with values.reshape(-1,1)

    data = pd.read_csv("./houses.csv", header=None, thousands='.')
    # data = pd.read_csv("./houses.csv", header=None)
    testData = pd.read_csv("./houses_test.csv", header=None)
    # Add code to remove houses less than 3000.
    testData.columns = ['living_space', 'size_of_property', 'price']
    data.columns = ['living_space', 'size_of_property', 'price']

    model = linear_model.LinearRegression()
    model.fit(data[['living_space', 'size_of_property']], data.price)

    predicted_prices = model.predict(testData[['living_space', 'size_of_property']])


    err = np.mean(np.abs(predicted_prices-testData.price))
    print(f"MAE {err}")


    # High error @ 300k. Need to visualise to fix. (It was those damn outliers!).
    fig = plt.figure()
    ax = fig.add_subplot(data.iloc[:,0], data.iloc[:,1], data.iloc[:,2], c='red')

    x
    y

    x_plot
    y_plot
    X
    Z

    ax.plot_wireframe(X,Y,Z)
    plt,show()

if __name__ == "__main__":
    myCode()