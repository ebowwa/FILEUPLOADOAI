import os
import time
import csv
import google.generativeai as genai

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

def save_to_csv(file_name, data):
    with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['x', 'y', 'z']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            response = model.generate_content(item["x"])  # Generate content for x
            item["z"] = response.text  # Set z as the response of the generated content
            writer.writerow(item)  # Write to CSV

# Example usage:
data = [
    {"x": "How do I bake a cake?", "y": "completion_1", "z": "combined_completion_1"},
    {"x": "How do I cook pasta?", "y": "completion_2", "z": "combined_completion_2"}
]
save_to_csv('dataset.csv', data)