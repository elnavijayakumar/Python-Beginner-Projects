# python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kilograms/pounds): ")

if unit == "kilograms":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "pounds":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print("NOT a valid unit")

print(f"Your weight is: {weight} {unit}")