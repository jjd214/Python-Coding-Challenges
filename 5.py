def main():
    start = float(input("Enter first odometer reading (miles): "))
    end = float(input("Enter second odometer reading (miles): "))
    gallons = float(input("Enter amount of gallons: "))

    miles_per_gallon = abs((end - start) / gallons)

    print(f"{miles_per_gallon:.1f} miles per gallon")
    print(f"{235.215 / miles_per_gallon:.2f} liters per 100 kilometers")

main()
