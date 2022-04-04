import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
def myCode(inputDegree):
    data = pd.read_csv("./houses.csv",header=None)
    data.columns = ['living_space','size_of_property','price']
    degree = inputDegree

    model = np.poly1d(np.polyfit(data.living_space, data.price, degree))
    predicted_prices = model(data.living_space)
    print_data = np.linspace(0, np.max(data.living_space),100)

    plt.figure()
    # plt.scatter(data.living_space,data.price)
    # plt.plot(print_data,model(print_data),c="black")
    # plt.ylim(min(data.price)*0.8,max(data.price)*1.2)


    err = np.mean(np.abs(predicted_prices-data.price))
    print(f'The MAE is {err}')
    house280 = model(280)
    print(f'The prediction for a house of size 280 is {house280}')

    # testing on new data
    newHouses  = pd.read_csv("./houses_test.csv")
    # Add collumns
    newHouses.columns = ['living_space','size_of_property','price']
    # Scatter inputs from the living space with the prediction
    plt.scatter(newHouses.living_space, model(newHouses.living_space),c="black")
    plt.show()

if __name__ == "__main__":
    myCode(5)
    myCode(3)
    myCode(10)