import json


def load_data(file_path):
    """Load animal data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_animals_html(data):
    """Generate HTML list items for animals."""
    output = ""

    for animal in data:
        output += "<li>\n"

        # Name
        name = animal.get("name")
        if name:
            output += f"Name: {name}<br>\n"

        # Characteristics
        characteristics = animal.get("characteristics", {})

        # Diet
        diet = characteristics.get("diet")
        if diet:
            output += f"Diet: {diet}<br>\n"

        # Location
        locations = animal.get("locations")
        if locations:
            output += f"Location: {locations[0]}<br>\n"

        # Type
        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}<br>\n"

        output += "</li>\n"

    return output


def main():
    data = load_data("animals_data.json")

    # Generate animal HTML
    animals_html = generate_animals_html(data)

    # Load template
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template = file.read()

    # Replace placeholder
    final_html = template.replace("_replace_animal_info", animals_html)

    # Write output file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("HTML file created successfully!")


if __name__ == "__main__":
    main()