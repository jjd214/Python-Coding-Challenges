C1, C2, C3, C4, EXP, F_CONV, F_OFFSET = 35.74, 0.6215, 35.75, 0.4275, 0.16, 9/5, 32

def calculate_wind_chill(T, V):
    return C1 + (C2 * T) - (C3 * (V ** EXP)) + (C4 * T * (V ** EXP))

def celsius_to_fahrenheit(T):
    return (T * F_CONV) + F_OFFSET

T = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").upper()

if unit == "C":
    T = celsius_to_fahrenheit(T)

for V in range(5, 65, 5):
    print(f"At temperature {T:.1f}F, and wind speed {V} mph, the wind chill is : {calculate_wind_chill(T,V):.2f}F")
