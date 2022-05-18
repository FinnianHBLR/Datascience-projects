import numpy as np
import pandas as pd
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def runCode():
    print('Lo')
    responses = pd.read_csv('responses_subset.csv')
    # print(responses.head())

    X = responses.drop('Age', axis=1)
    # print(X)
    y = responses.Age >= 19

    X = X.loc[:, X.dtypes != 'object'].copy()

    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

    model = XGBClassifier()
    model.fit(Xtrain, Ytrain)

    pred = model.predict(Xtest)
    print(pred)

    from sklearn.metrics import confusion_matrix
    print(confusion_matrix(Ytest, pred))
    tn, fp, fn, tp = confusion_matrix(Ytest, pred).ravel()

    # We want to show the probability now
    pred_proba = model.predict_proba(Xtest)

    fpr, tpr, thresholds = metrics.roc_curve(Ytest, pred_proba[:,0])

    import matplotlib.pyplot as plt
    plt.plot(tpr, fpr)
    plt.ylabel('True positive rate')
    plt.xlabel('False positive rate')
    plt.show()

if __name__ == '__main__':
    runCode()