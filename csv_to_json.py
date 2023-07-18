import pandas as pd

#Replace 'input.csv' with the path to your CSV file.
input_csv = 'input.csv'

#Replace 'output.json' with the desired path for your JSON file.
output_json = 'output.json'

#Read the CSV file into a pandas DataFrame
data_frame = pd.read_csv(input_csv)

#convert the DataFrame to a JSON object and save it to a file.
data_frame.to_json(output_json, orient='records' , lines=True)

