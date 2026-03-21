import json
import os
print(os.path.abspath("filtered_animal.html"))



def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    ...
    return output

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


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
        name = animal.get("name")
        diet = animal.get("diet")
        locations = animal.get("locations")
        animal_type = animal.get("type")
        lifespan = animal.get("lifespan")
        habitat = animal.get("habitat")
        behavior = animal.get("behavior")
        geographic = animal.get("geographic_range")
        image_url = animal.get("image_url")
        reproduction = animal.get("reproduction")

        if name:
            print(f"Name: {name}")

        if diet:
            print(f"Diet: {diet}")

        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")

        if animal_type:
            print(f"Type: {animal_type}")



print_animals_data("animals_data.json")



with open("animals_template.html", "r") as file_path:
    animals = file_path.read()
    print(animals)



animal_html = animals.replace('_replace_animal_info', "_animals")
print(animal_html)

with open("filtered_animals.html", "w") as file_out:
    animal_html = file_out.write(animal_html)


def generate_animals_string(data):
    """
    Generate a formatted string with animal data.
    """
    # ✅ FIXED LOOP + .get()
    #output += serialize_animal(animal)
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)

    animal_type = characteristics.get("type")
    if animal_type:
        output += f"Type: {animal_type}\n"


    output += '<li class="cards__item">\n'

    output += f'<img src="images/arctic_fox.jpg" alt="Arctic Fox" class="card__image"/>\n'
    output += f'<h2 class="card__title">Arctic Fox</h2>\n'

    output += '<div class="card__text">\n'

    output += f"Lifespan: {lifespan}\n"
    output += f"Habitat: {habitat}\n"
    output += f"Behavior: {behavior}\n"
    output += f"Geographic_Range:{Geographic_Range}\n"
    output += f"Image_URL:{Image_URL}\n"
    output += f"Reproduction: {reproduction}\n"

    output += '</div>\n'

    output += '</li>\n'



    output += "\n"

    return output



# Load your JSON data
data = load_data("animals_data.json")


# Load JSON data
with open("animals_data.json", "r") as file:
    animals = json.load(file)

# Normalize keys to lowercase for safety
animals = [{k.lower(): v for k, v in animal.items()} for animal in animals]

# Extract unique skin_type values (ignore missing)
skin_types = sorted({animal.get("skin_type") for animal in animals if animal.get("skin_type")})
print("Available skin types:")
for current_skin in skin_types:
    print(f"- {current_skin}")

# Prompt user to choose a skin_type
selected_skin = input("\nEnter a skin type from the list above: ").strip()

# Filter animals with the selected skin_type
filtered_animals = [a for a in animals if a.get("skin_type") == selected_skin]

if not filtered_animals:
    print(f"No animals found with skin type '{selected_skin}'.")
else:
    print(f"\nGenerating website for animals with skin type '{selected_skin}'...\n")


    html_content += f"""  <li class="cards__item">
    <div class="card__title">{name}</div>
    <div class="card__text">
      <ul class="animal-details">
        <li><strong>Diet:</strong> {diet}</li>
        <li><strong>Location:</strong> {location}</li>
        <li><strong>Type:</strong> {animal_type}</li>
        <li><strong>Type:</strong> {skin_type}</li>
      </ul>
    </div>
  </li>\n"""
    html_content += "</ul>"

    # Save to file
    with open("filtered_animals.html", "w") as file:
        file.write(html_content)
    print("Website generated: filtered_animals.html")

# Initialize output
output = ""

# Loop over each animal and generate <li> HTML
for animal_data in data:
    output += '<li class="cards__item">\n'

    # Name
    name = animal_data.get("name", "Unknown")
    output += f"Name: {name}<br/>\n"

    # Diet
    characteristics = animal_data.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    output += f"Diet: {diet}<br/>\n"

    # Location
    locations = animal_data.get("locations", ["Unknown"])
    output += f"Location: {locations[0]}<br/>\n"

    # Type
    animal_type = characteristics.get("type", "Unknown")
    output += f"Type: {animal_type}<br/>\n"

    # Close the list item
    output += "</li>\n"

# Print for verification
print(output)

# Generate HTML list items dynamically from output
# Assume output is already generated as HTML <li> elements
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
