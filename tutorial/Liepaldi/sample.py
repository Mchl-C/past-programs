import json

with open('data.json', 'r') as file:
    loaded_data = json.load(file)  # Returns Python object

print(loaded_data) 
