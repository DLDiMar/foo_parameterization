import csv
import os
from datetime import datetime
import getpass

def log_result(shape, param1_name, param1_value, param2_name="", param2_value="", param3_name="", param3_value="", volume_output=""):
    # Ensure the csv_outputs directory exists
    output_dir = "csv_outputs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create the filename
    filename = os.path.join(output_dir, f"{getpass.getuser()}-foo_parameterization_results-{datetime.now().strftime('%Y-%m-%d "%Y-%m-%d %H:%M:%S"')}.csv")
    file_exists = os.path.isfile(filename)
    
    # Define the field names for the CSV file
    fieldnames = ['date', 'username', 'shape', 'param1_name', 'param1_value', 'param2_name', 'param2_value', 'param3_name', 'param3_value', 'volume_output']
    
    # Open the file in append mode and write the data
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'username': getpass.getuser(),
            'shape': shape,
            'param1_name': param1_name,
            'param1_value': param1_value,
            'param2_name': param2_name,
            'param2_value': param2_value,
            'param3_name': param3_name,
            'param3_value': param3_value,
            'volume_output': volume_output
        })
