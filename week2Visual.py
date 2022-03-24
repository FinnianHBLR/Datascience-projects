import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Print the coordinates of sales (in
# price_paid_records_small.csv) east
# and west of Greenwitch in green and
# red.
# • Plot Greenwitch as black circle

dfPricePaid = pd.read_csv("./price_paid_records_small.csv")

plt.figure()
plt.scatter(moreThan0Joined["longitude"], moreThan0Joined["latitude"])
#x = np.arange(5)
# y = x**2
# plt.plot(x,y)
# plt.plot(x,y+2)
# plt.scatter(x,y+3, marker="d", c="g", s=100)

# For only greenwithc plt.scatter(readData["longitude"], readData["latitude"])


plt.show()