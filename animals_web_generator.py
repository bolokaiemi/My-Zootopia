import json


# =========================
# LOAD FUNCTIONS
# =========================

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(file_path):
    """Load HTML template."""
    with open(file_path, "r") as file:
        return file.read()


# =========================
# SKIN TYPE UTILITIES
# =========================

def get_skin_type(animal):
    """Safely extract skin_type from an animal object."""
    return animal.get("characteristics", {}).get("skin_type", "Unknown")


def list_skin_types(animals):
    """Return sorted unique skin types."""
    return sorted({
        get_skin_type(animal)
        for animal in animals
        if get_skin_type(animal) != "Unknown"
    })


def filter_by_skin_type(animals, selected_skin):
    """Filter animals by skin type (case-insensitive)."""
    selected_skin = selected_skin.lower()
    return [
        animal for animal in animals
        if get_skin_type(animal).lower() == selected_skin
    ]


def print_skin_types(animals):
    """Print available skin types."""
    print("Available skin types:")
    for skin in list_skin_types(animals):
        print(f"- {skin}")


# =========================
# HTML GENERATION
# =========================

def serialize_animal(animal):
    """Convert a single animal into HTML."""
    characteristics = animal.get("characteristics", {})

    name = animal.get("name", "Unknown")
    diet = characteristics.get("diet", "Unknown")
    location = animal.get("locations", ["Unknown"])[0]
    animal_type = characteristics.get("type", "Unknown")
    skin_type = get_skin_type(animal)

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <div class="card__text">
            <ul class="animal-details">
                <li><strong>Diet:</strong> {diet}</li>
                <li><strong>Location:</strong> {location}</li>
                <li><strong>Type:</strong> {animal_type}</li>
                <li><strong>Skin Type:</strong> {skin_type}</li>
            </ul>
        </div>
    </li>
    """


def generate_animals_html(data):
    """Generate HTML list for animals."""
    return "".join(serialize_animal(animal) for animal in data)


# =========================
# MAIN PROGRAM
# =========================

def main():
    # Load data
    animals_data = load_data("animals_data.json")

    # --- PRINT SIMPLE SKIN TYPE INFO ---
    print("\nSimple Skin Type Info:")
    for animal in animals_data:
        name = animal.get("name", "Unknown")
        skin_type = get_skin_type(animal)
        print(f"{name}: Skin Type = {skin_type}")

    # Show available skin types
    print_skin_types(animals_data)

    # Create mapping for smart matching (lowercase -> original)
    valid_skins = {skin.lower(): skin for skin in list_skin_types(animals_data)}

    # User input (cleaned)
    selected_skin = input("\nEnter a skin type (or press Enter to show all): ").strip().lower()

    # Apply filter only if user typed something
    if selected_skin:
        if selected_skin not in valid_skins:
            print(f"Invalid skin type: '{selected_skin}'")
            return

        # Convert back to proper format (e.g. "fur" -> "Fur")
        selected_skin_proper = valid_skins[selected_skin]

        animals_data = filter_by_skin_type(animals_data, selected_skin_proper)

        if not animals_data:
            print(f"No animals found with skin type '{selected_skin_proper}'")
            return

    # Load template
    template = load_template("animals_template.html")

    # Generate HTML
    animals_html = generate_animals_html(animals_data)

    # Replace placeholder
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    # Write output file
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(final_html)

    print("\n✅ Website successfully generated: animals.html")


# =========================

if __name__ == "__main__":
    main()