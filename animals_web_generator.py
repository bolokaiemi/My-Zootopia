import json

with open("animals_data.json", "r") as file_path:
    data = json.load(file_path)
    print(data)

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


