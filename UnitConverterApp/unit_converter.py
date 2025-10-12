def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    factors = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }

    if from_unit not in factors or to_unit not in factors:
        return "Invalid unit provided."

    # Convert to meters first
    value_in_meters = value * factors[from_unit]

    # Convert from meters to target unit
    converted_value = value_in_meters / factors[to_unit]
    return converted_value

def convert_weight(value, from_unit, to_unit):
    # Conversion factors to kilograms
    factors = {
        'kilogram': 1,
        'gram': 0.001,
        'pound': 0.453592,
        'ounce': 0.0283495
    }

    if from_unit not in factors or to_unit not in factors:
        return "Invalid unit provided."

    # Convert to kilograms first
    value_in_kg = value * factors[from_unit]

    # Convert from kilograms to target unit
    converted_value = value_in_kg / factors[to_unit]
    return converted_value

def main():
    print("Welcome to the Unit Converter!")
    print("Available conversions:")
    print("1. Length (meter, kilometer, centimeter, millimeter, mile, yard, foot, inch)")
    print("2. Weight (kilogram, gram, pound, ounce)")

    category = input("Enter conversion category (Length/Weight): ").lower()

    if category == 'length':
        try:
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError:
            print("Invalid value. Please enter a number.")
    elif category == 'weight':
        try:
            value = float(input("Enter the value to convert: "))
            from_unit = input("Enter the unit to convert from: ").lower()
            to_unit = input("Enter the unit to convert to: ").lower()
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        except ValueError:
            print("Invalid value. Please enter a number.")
    else:
        print("Invalid category. Please choose Length or Weight.")

if __name__ == "__main__":
    main()