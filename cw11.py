from datetime import datetime
import json

# Function that returns trip details as a dictionary
def get_trip(city, visit_date, comment):
    return {
        "city": city,
        "visit_date": visit_date,  # in dd-mm-yyyy format
        "comment": comment
    }

# Build a list of trip dictionaries
trips = [
    get_trip("London", "15-05-2023", "Visited Big Ben and London Eye."),
    get_trip("Rome", "22-08-2022", "Explored the Colosseum."),
    get_trip("Dubai", "10-12-2024", "Desert safari was amazing!")
]

# Convert date string → date object → formatted date
for trip in trips:
    # Convert string to date object
    date_obj = datetime.strptime(trip["visit_date"], "%d-%m-%Y")
    
    # Format date as "Month Day, Year"
    formatted_date = date_obj.strftime("%B %d, %Y")
    
    # Update dictionary with formatted date
    trip["visit_date"] = formatted_date

# Convert list of trips to JSON string
json_output = json.dumps(trips, indent=4)

# Print JSON string
print("JSON Output:")
print(json_output)