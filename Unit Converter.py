# unit_converter.py

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(lb):
    return lb / 2.20462


def main():
    print("----- Unit Converter -----")
    print("1. Kilometers ↔ Miles")
    print("2. Celsius ↔ Fahrenheit")
    print("3. Kilograms ↔ Pounds")
    print("0. Exit")

    while True:
        choice = input("\nChoose an option (0-3): ")

        if choice == "1":
            val = float(input("Enter value: "))
            direction = input("Convert to (m for miles, k for km): ").lower()
            if direction == "m":
                print(f"{val} km = {km_to_miles(val):.2f} miles")
            else:
                print(f"{val} miles = {miles_to_km(val):.2f} km")

        elif choice == "2":
            val = float(input("Enter value: "))
            direction = input("Convert to (f for Fahrenheit, c for Celsius): ").lower()
            if direction == "f":
                print(f"{val}°C = {celsius_to_fahrenheit(val):.2f}°F")
            else:
                print(f"{val}°F = {fahrenheit_to_celsius(val):.2f}°C")

        elif choice == "3":
            val = float(input("Enter value: "))
            direction = input("Convert to (p for pounds, k for kg): ").lower()
            if direction == "p":
                print(f"{val} kg = {kg_to_pounds(val):.2f} pounds")
            else:
                print(f"{val} pounds = {pounds_to_kg(val):.2f} kg")

        elif choice == "0":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
