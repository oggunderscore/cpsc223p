from flights import Flights


def main():
    filename = "data.json"
    flight_schedule = Flights(filename)

    while True:
        print("*** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
        print("1. Add flight")
        print("2. Print flight schedule")
        print("3. Set flight schedule filename")
        print("9. Exit the program")

        choice = input("Enter menu choice: ")

        if choice == "1":
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            flight_number = input("Enter flight number: ")
            departure = input("Enter departure time (HHMM): ")
            next_day = input("Is arrival next day (Y/N): ")
            arrival = input("Enter arrival time (HHMM): ")

            if flight_schedule.add_flight(
                origin, destination, flight_number, departure, next_day, arrival
            ):
                print("Flight added successfully.")
            else:
                print("Invalid time format. Flight not added.")

        elif choice == "2":
            flights = flight_schedule.get_flights()
            print("================== FLIGHT SCHEDULE ==================")
            print("Origin Destination Number Departure Arrival Duration")
            print("====== =========== ====== ========= ======== ========")
            for flight in flights:
                print(
                    f"{flight['origin']} {flight['destination']} {flight['flight_number']} "
                    f"{flight['departure']} {flight['arrival']} {flight['duration']}"
                )

        elif choice == "3":
            new_filename = input("Enter new flight schedule filename: ")
            flight_schedule = Flights(new_filename)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please enter a valid menu option.")


if __name__ == "__main__":
    main()
