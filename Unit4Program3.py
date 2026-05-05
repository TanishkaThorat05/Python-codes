import json
import csv

# Sample JSON data (array of objects)
data = [
    {"Name": "Alice", "Age": 20, "City": "Pune"},
    {"Name": "Bob", "Age": 22, "City": "Mumbai"},
    {"Name": "Charlie", "Age": 21, "City": "Delhi"}
]

# Write JSON data to CSV
with open("output.csv", "w", newline="") as file:
    # Extract field names (keys)
    fieldnames = data[0].keys()
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()   # Write column names
    writer.writerows(data) # Write data rows

print("JSON data successfully converted to CSV!")