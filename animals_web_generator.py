import json

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

with open("animals.html", "w") as file_out:
    animal_html = file_out.write(animal_html)


def generate_animals_string(data):
    """
    Generate a formatted string with animal data.
    """

    output = ""

    # ✅ FIXED LOOP + .get()
    for animal in load_data("animals_data.json"):
        name = animal.get("name")
        output += f"Name: {name}\n"

        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet")

        if diet:
            output += f"Diet: {diet}\n"

        locations = animal.get("locations")
        if locations:
            output += f"Location: {locations[0]}\n"

        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}\n"

        output += "\n"

    return output



# Load your JSON data
data = load_data("animals_data.json")

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

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file created!")
