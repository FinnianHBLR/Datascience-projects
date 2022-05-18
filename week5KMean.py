import pandas as pd
from sklearn.cluster import KMeans

def myCode():
    spendingData = pd.read_csv("./clustering_exercise.csv")

    model = KMeans(n_clusters=2)
    # Collumn 0 and 1.
    features = spendingData.iloc[:,[0,1]]
    model.fit(features)
    # model.cluster_centers_
    # model.cluster_centers_[0,:]
    # model.cluster_centers_[:,0]

    res = model.predict(features)

    import matplotlib.pyplot as plt

    plt.figure()
    plt.scatter(spendingData.meat_spending, spendingData.vegetable_spending, c=res)
    plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c="red", marker="D", s=100)
    plt.show()

    # show with prime mebership.
    plt.figure()
    plt.scatter(spendingData.meat_spending, spendingData.vegetable_spending, c=spendingData['prime_member']=='yes')
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], c="red", marker="D", s=100)
    plt.show()

    # To check if these observations in the actual world.
    confusion_matrix = pd.crosstab(spendingData['class'], res, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)

    confusion_matrix = pd.crosstab(spendingData['prime_member'], res, rownames=['Actual'], colnames=['Predicted'])
    print(confusion_matrix)
    # from sklearn.metrics

if __name__ == "__main__":
    myCode()