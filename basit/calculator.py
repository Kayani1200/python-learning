


# ===== UNIT CONVERTER =====

print("===== WELCOME TO UNIT CONVERTER =====")

print("\n1. Kilometer to Meter")
print("2. Meter to Kilometer")
print("3. Kilogram to Gram")
print("4. Gram to Kilogram")
print("5. Meter to Centimeter")
print("6. Celsius to Fahrenheit")

choice = int(input("\nSelect your conversion (1-6): "))

if choice == 1:
    kilometer = float(input("Enter kilometers: "))
    meter = kilometer * 1000
    print("Result:", meter, "Meters")

elif choice == 2:
    meter = float(input("Enter meters: "))
    kilometer = meter / 1000
    print("Result:", kilometer, "Kilometers")

elif choice == 3:
    kilogram = float(input("Enter kilograms: "))
    gram = kilogram * 1000
    print("Result:", gram, "Grams")

elif choice == 4:
    gram = float(input("Enter grams: "))
    kilogram = gram / 1000
    print("Result:", kilogram, "Kilograms")

elif choice == 5:
    meter = float(input("Enter meters: "))
    centimeter = meter * 100
    print("Result:", centimeter, "Centimeters")

elif choice == 6:
    celsius = float(input("Enter Celsius temperature: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Result:", fahrenheit, "Fahrenheit")

else:
    print("Invalid choice! Please select between 1 and 6.")

print("\n===== THANK YOU FOR USING UNIT CONVERTER =====")
