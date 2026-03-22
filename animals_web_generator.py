import json
import os

print(os.path.abspath("filtered_animal.html"))

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as file_out:
        return json.load(file_out)

def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj.get("name", "Unknown")}</div>\n'

    # ✅ FIX: get from characteristics
    characteristics = animal_obj.get("characteristics", {})
    skin_type = characteristics.get("skin_type", "Unknown")

    output += f'<div class="card__text">Skin Type: {skin_type}</div>\n'
    output += '</li>\n'

    return output


def main():
    print(load_data("animals_data.json"))

if __name__ == "__main__":
    main()


def print_animals_data(file_path):
    """
    Read animal data from a JSON file and print selected fields.
    """
    with open(file_path, "r") as file:
        animals = json.load(file)

    for animal in animals:
        characteristics = animal.get("characteristics", {})

        name = animal.get("name")
        diet = characteristics.get("diet")
        locations = animal.get("locations")
        animal_type = characteristics.get("type")
        skin_type = characteristics.get("skin_type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        if animal_type:
            print(f"Type: {animal_type}")
        if skin_type:
            print(f"Skin Type: {skin_type}")


print_animals_data("animals_data.json")


with open("animals_template.html", "r") as file_path:
    animals_template = file_path.read()
    print(animals_template)

animal_html = animals_template.replace('_replace_animal_info', "_animals")
print(animal_html)

with open("filtered_animals.html", "w") as file_out:
    file_out.write(animal_html)


def generate_animals_string(data):
    """
    Generate a formatted string with animal data.
    """
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


# Load your JSON data
data = load_data("animals_data.json")

# Load JSON data
with open("animals_data.json", "r") as file:
    animals = json.load(file)

# Normalize keys (top-level only)
animals = [{k.lower(): v for k, v in animal.items()} for animal in animals]

# ✅ FIX: Extract skin types from characteristics
skin_types = sorted({
    animal.get("characteristics", {}).get("skin_type")
    for animal in animals
    if animal.get("characteristics", {}).get("skin_type")
})

print("Available skin types:")
for current_skin in skin_types:
    print(f"- {current_skin}")

# Prompt user
selected_skin = input("\nEnter a skin type from the list above: ").strip()

# ✅ FIX: Filter using characteristics
filtered_animals = [
    a for a in animals
    if a.get("characteristics", {}).get("skin_type") == selected_skin
]

if not filtered_animals:
    print(f"No animals found with skin type '{selected_skin}'.")
else:
    print(f"\nGenerating website for animals with skin type '{selected_skin}'...\n")

    html_content = "<ul>\n"

    for animal in filtered_animals:
        characteristics = animal.get("characteristics", {})

        name = animal.get("name", "Unknown")
        diet = characteristics.get("diet", "Unknown")
        location = animal.get("locations", ["Unknown"])[0]
        animal_type = characteristics.get("type", "Unknown")
        skin_type = characteristics.get("skin_type", "Unknown")

        html_content += f"""  <li class="cards__item">
    <div class="card__title">{name}</div>
    <div class="card__text">
      <ul class="animal-details">
        <li><strong>Diet:</strong> {diet}</li>
        <li><strong>Location:</strong> {location}</li>
        <li><strong>Type:</strong> {animal_type}</li>
        <li><strong>Skin Type:</strong> {skin_type}</li>
      </ul>
    </div>
  </li>\n"""

    html_content += "</ul>"

    # Save file
    with open("filtered_animals.html", "w") as file:
        file.write(html_content)

    print("Website generated: filtered_animals.html")


# Initialize output
output = ""

# Loop over each animal
for animal_data in data:
    output += '<li class="cards__item">\n'

    name = animal_data.get("name", "Unknown")
    output += f"Name: {name}<br/>\n"

    characteristics = animal_data.get("characteristics", {})

    diet = characteristics.get("diet", "Unknown")
    output += f"Diet: {diet}<br/>\n"

    locations = animal_data.get("locations", ["Unknown"])
    output += f"Location: {locations[0]}<br/>\n"

    animal_type = characteristics.get("type", "Unknown")
    output += f"Type: {animal_type}<br/>\n"

    # ✅ FIX: Skin type from characteristics
    skin_type = characteristics.get("skin_type", "Unknown")
    output += f"Skin Type: {skin_type}<br/>\n"

    output += "</li>\n"

print(output)

# Final HTML
html_content = f"""
<body>
    <h1>My Animal Repository</h1>
    <ul class="cards">
        {output.replace('\n', '<br>')}
    </ul>
</body>
"""

with open("filtered_animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file created!")