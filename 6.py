from datetime import datetime

def main():
    gender = input("Enter your gender (M/F): ").upper()
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight (lbs): "))
    inches = float(input("Enter your height (inches): "))

    age = compute_age(birthdate)
    kg, cm = pounds * 0.45359237, inches * 2.54
    bmi = kg / (cm / 100) ** 2

    if gender == "F":
        bmr = 447.593 + 9.247 * kg + 3.098 * cm - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * kg + 4.799 * cm - 5.677 * age

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mas index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

def compute_age(birthdate):
    birth = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.now()
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

main()
