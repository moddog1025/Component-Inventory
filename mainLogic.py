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

def main():
    components = ["Resistor", "Capacitor", "Diode", "LED", "LDO", "Crystal", "Sensor", "Microcontroller"]
    print("Please choose a component type by entering a number (1-8):")
    for i, component in enumerate(components, 1):
        print(f"{i}. {component}")

    choice = int(input("Enter your choice (1-8): "))
    if choice < 1 or choice > 8:
        print("Invalid choice. Please enter a number between 1 and 8.")
        return

    component_type = components[choice - 1]

    if component_type == "Resistor":
        resistor_value_input = input("Enter the resistance (e.g., 2000, 2k, 2K, 1M, 20R): ")
        try:
            resistor_value = convert_resistance_value(resistor_value_input)
            print(f"Stored resistance value: {resistor_value} ohms.")
        except ValueError:
            print("Invalid resistance value. Please enter a valid number.")

if __name__ == "__main__":
    main()

