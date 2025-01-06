value1 = 35.74
value2 = 0.6215
value3= 35.75
value4 = 0.4275
value5 = 9/5
value6 = 32
exponent = 0.16
def calculate_wind_chill(T, V):
    wind_chill = value1 + (value2 * T) - (value3 * (V**exponent)) + (value4*T) * (V**exponent)
    return wind_chill

def celsius_to_fahrenheit(T):
    fahrenheit = (T * value5) + value6
    return fahrenheit

T = float(input("What is the temperature? "))
user = input("Fahrenheit or Celsius (F/C)? ").upper()

V = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

for i in V:

    if user == "C":
        new_temp = celsius_to_fahrenheit(T)
        wind_chill = calculate_wind_chill(new_temp, i)

    elif user == "F":
        new_temp = T
        wind_chill = calculate_wind_chill(T, i)

    print(f"At temperature {new_temp:.1f}F, and wind speed {i} mph, the windchill is : {wind_chill:.2f}F")


# # Constants
# C1, C2, C3, C4, EXP, F_CONV, F_OFFSET = 35.74, 0.6215, 35.75, 0.4275, 0.16, 9 / 5, 32

# # Functions
# def calculate_wind_chill(T, V):
#     return C1 + (C2 * T) - (C3 * (V**EXP)) + (C4 * T * (V**EXP))

# def celsius_to_fahrenheit(T):
#     return (T * F_CONV) + F_OFFSET

# # User input
# T = float(input("Temperature? "))
# unit = input("Fahrenheit or Celsius (F/C)? ").upper()
# if unit == "C":
#     T = celsius_to_fahrenheit(T)

# # Calculate and print wind chill for wind speeds
# for V in range(5, 65, 5):
#     print(f"At {T:.1f}°F and {V} mph, wind chill: {calculate_wind_chill(T, V):.2f}°F")
