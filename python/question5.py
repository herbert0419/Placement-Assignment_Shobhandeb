import requests
import pandas as pd
import json

# Download the data from the provided API link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Extract the required data attributes
show_id = data["id"]
show_url = data["url"]
show_name = data["name"]

episodes = data["_embedded"]["episodes"]
episode_data = []
for episode in episodes:
    episode_data.append({
        "season": episode["season"],
        "number": episode["number"],
        "type": episode["type"],
        "airdate": episode["airdate"],
        "airtime": episode["airtime"],
        "runtime": episode["runtime"],
        "average_rating": episode["rating"]["average"],
        "summary": episode["summary"].strip("<p>").strip("</p>"),
        "medium_image_link": episode["image"]["medium"],
        "original_image_link": episode["image"]["original"]
    })

# Print the extracted data attributes
for episode in episode_data:
    print(f"Season: {episode['season']}")
    print(f"Episode: {episode['number']}")
    print(f"Type: {episode['type']}")
    print(f"Airdate: {episode['airdate']}")
    print(f"Airtime: {episode['airtime']}")
    print(f"Runtime: {episode['runtime']} minutes")
    print(f"Average Rating: {episode['average_rating']}")
    print(f"Summary: {episode['summary']}")
    print(f"Medium Image Link: {episode['medium_image_link']}")
    print(f"Original Image Link: {episode['original_image_link']}")
    print()

# Save the extracted data in CSV format
csv_filename = "episode_data.csv"
df = pd.DataFrame(episode_data)
df.to_csv(csv_filename, index=False)
print(f"Data successfully saved as CSV: {csv_filename}")

# Save the extracted data in JSON format
json_filename = "episode_data.json"
with open(json_filename, "w") as f:
    json.dump(episode_data, f, indent=4)
print(f"Data successfully saved as JSON: {json_filename}")