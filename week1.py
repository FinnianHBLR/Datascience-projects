import pandas as pd
data = pd.DataFrame([[1, 100, 10, 'OOC'], [2, 200, 30, 'TIL'], [3, 123, 11, 'OOC'], [4, 400, 99, 'SJO']], columns=['orderID', 'componentA', 'componentB', 'customer'])

def start():
    print('We are a juice manufacturer!')
    # multiply and create new col

    # If you dont use .values it will be a series
    data['shipment'] = data.componentA.values * 10 + data.componentB.values * 15
    print(data['shipment'].sum());
    # Get data from OOC company only.
    print(data.loc[(data.customer == 'OOC'), 'shipment'])

    # data['avg_ship'] = data.componentA.mean()
    average = (data.componentA * 15).mean()
    # print(data['avg_ship'])
    print(average)

if __name__ == '__main__':
    start()
