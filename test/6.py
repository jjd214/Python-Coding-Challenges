from datetime import datetime

def main():
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    pounds = float(input("Enter your weight in US pounds: "))
    inches = float(input("Enter your height in US inches: "))

    years = compute_age(birthdate)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)

    print(f"Age (years): {years}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")


def compute_age(birth):
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    years = today.year - birthday.year

    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    kg = lb * 0.45359237
    return kg


def cm_from_in(inch):
    cm = inch * 2.54
    return cm


def body_mass_index(weight, height):
    bmi = weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper() == "F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr


main()


# from datetime import datetime

# def main():
#     gender = input("Enter your gender (M/F): ").upper()
#     birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
#     pounds = float(input("Enter your weight (lbs): "))
#     inches = float(input("Enter your height (inches): "))

#     age = compute_age(birthdate)
#     kg, cm = pounds * 0.45359237, inches * 2.54
#     bmi = kg / (cm / 100) ** 2

#     if gender == "F":
#         bmr = 447.593 + 9.247 * kg + 3.098 * cm - 4.330 * age
#     else:
#         bmr = 88.362 + 13.397 * kg + 4.799 * cm - 5.677 * age

#     print(f"Age (years): {age}")
#     print(f"Weight (kg): {kg:.2f}")
#     print(f"Height (cm): {cm:.1f}")
#     print(f"Body mas index: {bmi:.1f}")
#     print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

# def compute_age(birthdate):
#     birth = datetime.strptime(birthdate, "%Y-%m-%d")
#     today = datetime.now()
#     return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# main()
