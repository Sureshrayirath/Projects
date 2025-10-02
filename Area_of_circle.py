import math

def calculate_circle_area():
    """
    Calculates the area of a circle based on user-provided radius.
    Formula: Area = π * r^2
    """
    print("--- Circle Area Calculator ---")
    
    
    try:
        radius_input = input("Enter the radius of the circle (e.g., 5.5): ")
        radius = float(radius_input)
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
        return

    #  Input Validation: Check for a non-negative radius
    if radius < 0:
        print("The radius cannot be a negative number.")
        return

    
    area = math.pi * (radius ** 2)

    
    print(f"\nRadius (r): {radius}")
    print(f"Pi (π):     {math.pi:.5f}")
    print(f"The Area of the Circle is: {area:.2f} square units.")
    print("----------------------------")

# Call the function to run the program
if __name__ == "__main__":
    calculate_circle_area()