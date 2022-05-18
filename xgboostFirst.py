import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from xgboostFirst import XGBRegressor
import matplotlib.pyplot as plt
from xgboostFirst import plot_tree
from sklearn import datasets

# Read data

fishData = pd.read_csv('Fish2.csv')

fishData.drop('Species', axis=1, inplace=True)

print(fishData)

# X is everything without weight
X = fishData.iloc[:, 0:20]
y = fishData.iloc[:, [21]]

# X Y train test
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)


model = XGBRegressor()
model.fit(Xtrain,Ytrain)
pred = model.predict(Xtest)

plt.scatter(Ytest,pred)
plt.xlabel("actual")
plt.ylabel("predicted")
mae = metrics.mean_absolute_error(Ytest, pred)
plt.show()
print('MAE: ' +str(mae))