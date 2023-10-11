from weather import *

default_filename = "w.dat"

weather_data = {}

while True:
    menu = "\n== Weather App ==\n\n1. Set data filename\n2. Add weather data\n3. Print daily report\n4. Print historical report\n5. Exit"
    print(menu)

    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the filename: ")
        weather_data = read_data(filename)
        print("Data loaded successfully!\n")

    elif choice == "2":
        date = input("Enter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temperature = float(input("Enter the temperature (°F): "))
        humidity = float(input("Enter the humidity (%): "))
        rainfall = float(input("Enter the rainfall (mm): "))

        key = f"{date}{time}"
        weather_data[key] = {
            "t": temperature,
            "h": humidity,
            "r": rainfall,
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
