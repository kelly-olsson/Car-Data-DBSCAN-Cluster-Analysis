import pandas as pd
import numpy as np

# Load your original dataset
data = pd.read_csv('data.csv')  # original data file path

# Identify categorical and non-categorical columns
categorical_columns = ["is_new", "fuel_id", "doors", "transmission_id", "body_style_id", "model_id"]
non_categorical_columns = ["model_year", "km", "price"]

# Generate mock new data
num_new_rows = 100
mock_new_data = pd.DataFrame()

# For non-categorical data, generate random values within the range of original data
for col in non_categorical_columns:
    mock_new_data[col] = np.random.uniform(data[col].min(), data[col].max(), num_new_rows)

# For categorical data, randomly select from the original categories
for col in categorical_columns:
    mock_new_data[col] = np.random.choice(data[col].unique(), num_new_rows)

# Ensure correct data types
for col in data.columns:
    if col in mock_new_data.columns:
        mock_new_data[col] = mock_new_data[col].astype(data[col].dtype)

# Save the new mock data to a CSV file
mock_new_data.to_csv('mock_new_data.csv', index=False)
