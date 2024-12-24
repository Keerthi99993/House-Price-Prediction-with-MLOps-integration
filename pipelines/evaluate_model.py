'''import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

def evaluate():
    print("Evaluating the model...")

    # Load the test data
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv").values.ravel()

    # Load the trained model
    model = joblib.load("models/random_forest_model.pkl")

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    evaluate()'''


import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer

def evaluate():
    print("Evaluating the model...")

    # Load the test data
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv").values.ravel()

    # Handle missing values in the test data
    categorical_columns = X_test.select_dtypes(include=['object']).columns
    numerical_columns = X_test.select_dtypes(exclude=['object']).columns

    # Impute categorical columns with the most frequent value
    categorical_imputer = SimpleImputer(strategy='most_frequent')
    X_test[categorical_columns] = categorical_imputer.fit_transform(X_test[categorical_columns])

    # Impute numerical columns with the median value
    numerical_imputer = SimpleImputer(strategy='median')
    X_test[numerical_columns] = numerical_imputer.fit_transform(X_test[numerical_columns])

    # Convert categorical data to numeric codes (same as the training data)
    for col in categorical_columns:
        X_test[col] = X_test[col].astype("category").cat.codes  # Convert to numeric codes

    # Load the trained model
    model = joblib.load("models/random_forest_model.pkl")

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    evaluate()
