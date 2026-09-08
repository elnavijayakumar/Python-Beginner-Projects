# python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kilograms/pounds): ")

if unit == "kilograms":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight,1)} {unit}")
elif unit == "pounds":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight,1)} {unit}")
else:
    print("NOT a valid unit")
