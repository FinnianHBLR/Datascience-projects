import pandas as pd
import matplotlib.pyplot as plt


def start():
            # Open data files.
            dfPostCodes = pd.read_json("./postcodes.json")
            dfPostCodes.drop_duplicates(subset='town', inplace=True)

            dfPricePaid = pd.read_csv("./price_paid_records_small.csv")

            # Set all towns to uppercase.
            dfPostCodes['town'] = dfPostCodes['town'].str.upper()

            # Everything positive on latitude is east of Greenwich
            moreThan0 = dfPostCodes.loc[(dfPostCodes.longitude > 0),].copy()
            lessThan0 = dfPostCodes.loc[(dfPostCodes.longitude < 0),].copy()

            # Joins the filtered towns to the transaction data.
            moreThan0Joined = moreThan0.set_index("town").join(dfPricePaid.set_index("Town/City"), how='inner')
            lessThan0Joined = lessThan0.set_index("town").join(dfPricePaid.set_index("Town/City"), how='inner')

            # Alternate moreThan0Joined = moreThan0.set_index("Town/City").join(dfPricePaid.set_index("town"), how='inner')
            # Print all more/less than 0.
            print(f"Number of entries +0: {moreThan0Joined.shape}")
            print(f"Number of entries -0: {lessThan0Joined.shape}")

            # Show each of the datasets on a scatter plot.
            plt.figure()
            plt.scatter(moreThan0Joined["longitude"], moreThan0Joined["latitude"], c="r")
            plt.scatter(lessThan0Joined["longitude"], lessThan0Joined["latitude"], c="g")
            plt.show()

            # Save data to dataset
            moreThan0Joined.to_csv("output.csv", index=False)
            lessThan0Joined.to_csv("output.csv", index=False)

            print(f"Out of total: {dfPricePaid.shape}")

if __name__ == '__main__':
    start()
