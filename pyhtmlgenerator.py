import json

# Load JSON data
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Generate HTML <li> items for each animal
def generate_animal_html(data):
    output = ""
    for animal in data:
        output += '<li class="cards__item">\n'

        # Name
        name = animal.get("name", "Unknown")
        output += f"Name: {name}<br/>\n"

        # Diet
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "Unknown")
        output += f"Diet: {diet}<br/>\n"

        # Location
        locations = animal.get("locations", ["Unknown"])
        output += f"Location: {locations[0]}<br/>\n"

        # Type
        animal_type = characteristics.get("type", "Unknown")
        output += f"Type: {animal_type}<br/>\n"

        output += "</li>\n"
    return output

# Main program
def main():
    animals = load_data("animals_data.json")
    animals_html = generate_animal_html(animals)

    # Full HTML content
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Animal Repository</title>
    <style>
        html {{ background-color: #ffe9e9; }}
        body {{ font-family: Arial, sans-serif; width: 900px; margin: auto; }}
        h1 {{ text-align: center; font-size: 40pt; }}
        .cards {{ list-style: none; padding: 0; }}
        .cards__item {{
            background-color: white;
            border-radius: 0.25rem;
            box-shadow: 0 20px 40px -14px rgba(0,0,0,0.25);
            padding: 1rem;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <h1>My Animal Repository</h1>
    <ul class="cards">
        {animals_html}
    </ul>
</body>
</html>
"""

    # Save to HTML file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("HTML file created successfully!")

if __name__ == "__main__":
    main()