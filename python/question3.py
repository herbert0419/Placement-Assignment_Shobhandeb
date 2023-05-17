import requests
import pandas as pd

# Download the data from the provided link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Extract the required attributes from the data
pokemon_data = []
for pokemon in data["pokemon"]:
    attributes = {
        "id": pokemon["id"],
        "num": pokemon["num"],
        "name": pokemon["name"],
        "img": pokemon["img"],
        "type": ", ".join(pokemon["type"]),
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "candy": pokemon.get("candy", ""),
        "candy_count": pokemon.get("candy_count", ""),
        "egg": pokemon.get("egg", ""),
        "spawn_chance": pokemon.get("spawn_chance", ""),
        "avg_spawns": pokemon.get("avg_spawns", ""),
        "spawn_time": pokemon.get("spawn_time", ""),
        "multipliers": ", ".join(str(m) for m in pokemon.get("multipliers", [])),
        "weakness": ", ".join(pokemon.get("weaknesses", []))
    }
    pokemon_data.append(attributes)

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(pokemon_data)

# Save the DataFrame to an Excel file
output_path = "pokemon_data.xlsx"
df.to_excel(output_path, index=False)

print(f"Data successfully converted and saved to '{output_path}'.")
