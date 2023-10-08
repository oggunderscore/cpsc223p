from weather import *

# Default filename for JSON data
default_filename = "w.dat"

# Dictionary to hold weather data
weather_data = {}

while True:
    print("\nMenu:")
    print("1. Set data filename")
    print("2. Add weather data")
    print("3. Print daily report")
    print("4. Print historical report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the filename: ")
        weather_data = read_data(filename)
        print("Data loaded successfully!")

    elif choice == "2":
        date = input("Enter the date (YYYYMMDD): ")
        time = input("Enter the time (hhmmss): ")
        temperature = float(input("Enter the temperature (°C): "))
        humidity = float(input("Enter the humidity (%): "))
        rainfall = float(input("Enter the rainfall (mm): "))

        key = f"{date}{time}"
        weather_data[key] = {
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall,
        }

        write_data(weather_data, default_filename)
        print("Data added and saved successfully!")

    elif choice == "3":
        date = input("Enter the date (YYYYMMDD): ")
        report = report_daily(weather_data, date)
        print(report)

    elif choice == "4":
        report = report_historical(weather_data)
        print(report)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
