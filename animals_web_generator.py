import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def main():
    print(load_data("animals_data.json"))

if __name__ == "__main__":
    main()


print()
import json

def print_animals_data(file_path):
    """
    Read animal data from a JSON file and print selected fields.

    Prints:
    - Name
    - Diet
    - First location (if available)
    - Type

    Skips any field that does not exist.
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

        print()  # blank line between animals


# Run the function
print_animals_data("animals_data.json")

print()

with open("animals_template.html", "r") as file_path:
    animals = file_path.read()
    print(animals)


print(":::::::::::::::::::::::::::::::::")
animal_html =  animals.replace('_replace_animal_info', "_animals")
print( animal_html)

print("::::::::::::::::::::::::::::::::::::::.")
with open("animals.html", "w") as file_out:
    animal_html = file_out.write(animal_html)



print(":::::::::::::::::::::::::::::::::::::::::")
def generate_animals_string(data):
    """
    Generate a formatted string with animal data.
    """

    output = ""

    for animal_data in data:
        output += f"Name: {animal_data.get('name')}\n"

        characteristics = animal_data.get("characteristics", {})
        diet = characteristics.get("diet")

        if diet:
            output += f"Diet: {diet}\n"

        locations = animal_data.get("locations")
        if locations:
            output += f"Location: {locations[0]}\n"

        animal_type = characteristics.get("type")
        if animal_type:
            output += f"Type: {animal_type}\n"

        output += "\n"

    return output

#print(generate_animals_string(data))


print(":::::::::::::::::::::::::::::")

output = ""  # define an empty string

for animal_data in data:
    # Name
    name = animal_data.get("name")
    if name:
        output += f"Name: {name}\n"

    # Diet (inside characteristics)
    characteristics = animal_data.get("characteristics", {})
    diet = characteristics.get("diet")
    if diet:
        output += f"Diet: {diet}\n"

    # Location (first item in list)
    locations = animal_data.get("locations")
    if locations and len(locations) > 0:
        output += f"Location: {locations[0]}\n"

    # Type (inside characteristics)
    animal_type = characteristics.get("type")
    if animal_type:
        output += f"Type: {animal_type}\n"

    # Blank line between animals
    output += "\n"

print(output)

with open("animals.html", "w") as file_out:
    final_html = file_out.write(data)
    print(final_html)
