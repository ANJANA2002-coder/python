from datetime import datetime
import json

# Function to create a travel record
def create_record(city, comment, visit_date):
    return {
        "city": city,
        "comment": comment,
        "visit_date": visit_date
    }

# Create at least 3 travel records
records = [
    create_record("Paris", "Beautiful architecture and museums.", "05-06-2022"),
    create_record("Tokyo", "Amazing food and technology.", "12-09-2023"),
    create_record("New York", "Loved Times Square and Central Park.", "20-01-2024")
]

# Convert date format from 'dd-mm-yyyy' to 'Month Day, Year'
for record in records:
    date_obj = datetime.strptime(record["visit_date"], "%d-%m-%Y")
    record["visit_date"] = date_obj.strftime("%B %d, %Y")

# Convert list to JSON string
json_string = json.dumps(records, indent=4)

print("JSON Output:")
print(json_string)

# Parse JSON back to Python object
parsed_data = json.loads(json_string)

print("\nParsed Records (Each on Separate Line):")
for record in parsed_data:
    print(record)