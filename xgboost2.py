from xgboost import XGBRegressor
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split

def runCode():
    tripData = pd.read_csv('NY-02_short_header.csv')

    filtered = tripData.drop(['fare_amount', 'surcharge', 'mta_tax', 'tolls_amount', 'total_amount'], axis=1).copy()

    X = filtered.drop('tip_amount', axis=1)
    y = filtered.tip_amount

    X = X.loc[:, X.dtypes != 'object'].copy()

    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    model = XGBRegressor()
    model.fit(Xtrain,Ytrain)
    # NTOE TEST ON TESTING DATA THEN SCATTER THAT
    pred = model.predict(Xtest)

    plt.scatter(Ytest,pred)
    plt.xlabel("actual")
    plt.ylabel("predicted")
    mae = metrics.mean_absolute_error(Ytest, pred)
    plt.show()
    print('MAE: ' +str(mae))

if __name__ == '__main__':
    runCode()