import requests
import pandas as pd

# Download the data from the provided link
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Extract the required attributes from the data
meteorite_data = []
for meteorite in data:
    attributes = {
        "name": meteorite["name"],
        "id": meteorite["id"],
        "nametype": meteorite["nametype"],
        "recclass": meteorite["recclass"],
        "mass": float(meteorite.get("mass (g)", 0)),
        "year": pd.to_datetime(meteorite.get("year", "1900-01-01"), errors="coerce"),
        "reclat": float(meteorite.get("reclat", 0)),
        "reclong": float(meteorite.get("reclong", 0)),
        "coordinates": [0, 0]  # Default values for latitude and longitude
    }

    if "geolocation" in meteorite:
        attributes["coordinates"] = [
            int(meteorite["geolocation"].get("latitude", 0)),
            int(meteorite["geolocation"].get("longitude", 0))
        ]

    meteorite_data.append(attributes)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(meteorite_data)

# Save the DataFrame to a CSV file
output_path = "meteorite_data.csv"
df.to_csv(output_path, index=False)

print(f"Data successfully converted and saved to '{output_path}'.")
