def convert_resistance_value(input_value):
    """Convert resistance input to numeric value in ohms."""
    if input_value.lower().endswith('k'):
        return float(input_value[:-1]) * 1000
    elif input_value.lower().endswith('m'):
        return float(input_value[:-1]) * 1000000
    elif input_value.lower().endswith('r'):
        return float(input_value[:-1])
    else:
        return float(input_value)

def add_component_to_inventory(inventory, component_type, rating, specification, package, amount):
    """Add a new component to the inventory list."""
    component = {
        'Component': component_type,
        'Rating': rating,
        'Specification': specification,
        'Package': package,
        'Amount': amount
    }
    inventory.append(component)

def main():
    inventory = []  # List to store component dictionaries
    components = ["Resistor", "Capacitor", "Diode", "LED", "LDO", "Crystal", "Sensor", "Microcontroller"]
    print("Please choose a component type by entering a number (1-8):")
    for i, component in enumerate(components, 1):
        print(f"{i}. {component}")

    choice = int(input("Enter your choice (1-8): "))
    if choice < 1 or choice > 8:
        print("Invalid choice. Please enter a number between 1 and 8.")
        return

    component_type = components[choice - 1]

    # Common data for all components
    specification = input("Enter the specification: ")
    package = input("Enter the package type: ")
    amount = input("Enter the amount: ")

    # Specific data for resistors
    if component_type == "Resistor":
        resistor_value_input = input("Enter the resistance (e.g., 2000, 2k, 2K, 1M, 20R): ")
        try:
            resistor_value = convert_resistance_value(resistor_value_input)
            rating = f"{resistor_value} ohms"
            add_component_to_inventory(inventory, component_type, rating, specification, package, amount)
            print(f"Added {component_type} to inventory.")
        except ValueError:
            print("Invalid resistance value. Please enter a valid number.")

    # Placeholder for handling other component types
    # Add similar handling for capacitors, diodes, LEDs, etc., with appropriate rating input and conversion

    print("Current Inventory:")
    for item in inventory:
        print(item)

if __name__ == "__main__":
    main()
