import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import davies_bouldin_score
from sklearn import preprocessing


def myCode():

    spendingData = pd.read_csv("./cluster_spendings.csv")

    # data - mminium / max - min
    for column in spendingData:
        spendingData[column] = (spendingData[column] - np.min(spendingData[column])) / (np.max(spendingData[column]) - np.min(spendingData[column]))

    print(spendingData.columns)

    model = KMeans(n_clusters=2, random_state=42)
    # Getting columns 0-1
    features = spendingData.iloc[:,0:2]
    model.fit(features)
    res = model.predict(features)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(spendingData.iloc[:, 0], spendingData.iloc[:, 1], spendingData.iloc[:, 2], c=res)
    plt.show()

if __name__ == "__main__":
    myCode()