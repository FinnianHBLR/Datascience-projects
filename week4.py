# using size to predict price

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error

def myCode():
    data = pd.read_csv("./houses.csv")
    # Needs to reshape to be a 2D array with values.reshape(-1,1)
    x = data.iloc[:, 0].values.reshape(-1,1)
    print(x)
    y = data.iloc[:, 2].values.reshape(-1,1)
    print(y)

    # Fit model
    model = linear_model.LinearRegression()
    model.fit(x,y)

    # I think this is wrong.
    # should be np.mean(abs(predictied_prices-data.price))
    print(mean_squared_error(x, model.predict(x)))

    # Create random values to predict on. You can also just do this with the normal data.
    x_plot = np.arange(0, 968)
    x_plot = x_plot.reshape(-1, 1)
    # Predict on those points,
    # print(model.predict(x_plot))
    y_predicted = model.predict(x_plot)
    # Plot input, then output
    xIn = pd.Series(280).to_frame()
    yOut = model.predict(xIn)
    print(f"Price on 280: {yOut}")
    plt.scatter(xIn, yOut, color='k')

    # Scatter x and y
    plt.scatter(x, y)
    # Then plot the predicted line based of random numbers put into the model.
    plt.plot(x_plot, y_predicted, color='red')
    plt.show()


def hisCode():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import linear_model
    data = pd.read_csv("c:/data/houses.csv", header=None)
    data.columns = ['living_space', 'size_of_property', 'price']
    degree = 5
    model = np.poly1d(np.polyfit(data.living_space, data.price, degree))
    predicted_prices = model(data.living_space)
    print_data = np.linspace(0, np.max(data.living_space), 100)
    plt.figure()
    plt.scatter(data.living_space, data.price)
    plt.plot(print_data, model(print_data), c="black")
    plt.ylim(min(data.price) * 0.8, max(data.price) * 1.2)
    plt.show()
    err = np.mean(np.abs(predicted_prices - data.price))
    print(f'The MAE is {err}')
    house280 = model(280)
    print(f'The prediction for a house of size 280 is {house280}')



if __name__ == "__main__":
    myCode()
    # hisCode()

