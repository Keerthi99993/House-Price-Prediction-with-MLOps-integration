import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib
import os  # Import os to handle directories

def trainss():
    print("Training the model...")

    # Load the preprocessed data
    X_train = pd.read_csv("X_train.csv")
    y_train = pd.read_csv("y_train.csv").values.ravel()

    # Handle missing values
    # For categorical columns, use the most frequent value to impute missing values
    categorical_columns = X_train.select_dtypes(include=['object']).columns
    numerical_columns = X_train.select_dtypes(exclude=['object']).columns

    # Impute categorical columns with the most frequent value
    categorical_imputer = SimpleImputer(strategy='most_frequent')
    X_train[categorical_columns] = categorical_imputer.fit_transform(X_train[categorical_columns])

    # Impute numerical columns with the median value
    numerical_imputer = SimpleImputer(strategy='median')
    X_train[numerical_columns] = numerical_imputer.fit_transform(X_train[numerical_columns])

    # Handle non-numeric data by converting categorical data to numeric codes
    for col in categorical_columns:
        X_train[col] = X_train[col].astype("category").cat.codes  # Convert to numeric codes

    # Train a simple Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Ensure the 'models' directory exists
    os.makedirs("models", exist_ok=True)  # Create 'models' directory if it doesn't exist

    # Save the trained model
    joblib.dump(model, "models/random_forest_model.pkl")
    print("Model training complete. Saved the model to 'models/random_forest_model.pkl'.")

if __name__ == "__main__":
    trainss()