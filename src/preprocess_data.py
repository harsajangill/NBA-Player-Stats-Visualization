import pandas as pd


def clean_nba_data(file_path):
    # Load the CSV data into a pandas DataFrame, skipping the first row
    df = pd.read_csv(file_path, skiprows=1)

    # Set the correct column names
    df.columns = df.iloc[0]

    # Drop the row containing the column names
    df = df.drop(df.index[0])

    # Drop rows that contain only missing values
    df = df.dropna(how='all')

    # Fill in the missing values with 0
    df = df.fillna(0)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('output/cleaned_data.csv', index=False)

    return df


# Usage
cleaned_data = clean_nba_data('input/input.csv')
