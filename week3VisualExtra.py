import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm

import numpy as np

def start():
    stores = pd.read_csv("./stores.csv")
    #  Because matplotlib is really annoying you can't pass in a list of shapes.
    premium = stores.loc[(stores.premium_store == 1)].copy()
    notPremium = stores.loc[(stores.premium_store == 0)].copy()

    plt.figure()
    plt.scatter(premium["longitude"], premium["latitude"], marker='h', s=premium["sales_volume"], c=premium["marketing_cost"], cmap=plt.cm.RdYlGn)
    plt.scatter(notPremium["longitude"], notPremium["latitude"], marker='o', s=premium["sales_volume"], c=premium["marketing_cost"], cmap=plt.cm.RdYlGn)
    plt.show()


if __name__ == "__main__":
    start()

