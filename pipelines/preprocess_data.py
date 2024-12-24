import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess():
    print("Preprocessing data...")

    # Sample data (replace with actual dataset)
    data ="extracted_data/AmesHousing.csv"

    df=pd.read_csv(data)
    '''if data is not None:
        df=pd.DataFrame(data)
    else:
        print("None")'''

    # Splitting into features and labels
    X = df.drop(columns=["SalePrice"])
    y = df["SalePrice"]

    # Splitting into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save data to CSV files
    X_train.to_csv("X_train.csv", index=False)
    X_test.to_csv("X_test.csv", index=False)
    y_train.to_csv("y_train.csv", index=False)
    y_test.to_csv("y_test.csv", index=False)

    print("Data preprocessing complete. Saved train and test datasets.")

if __name__ == "__main__":
    preprocess()
