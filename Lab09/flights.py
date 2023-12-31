import json

# Flights Class


class Flights:
    # Default Constructor
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            # Validate data.json is usable json
            with open(filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    # Function to add flights to data
    def add_flight(
        self, origin, destination, flight_number, departure, next_day, arrival
    ):
        # Sanity Check
        if not self.is_valid_time(departure) or not self.is_valid_time(arrival):
            return False

        # Declare the var
        flight_data = {
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": departure,
            "next_day": next_day,
            "arrival": arrival,
        }

        # Add data to class
        self.data.append(flight_data)

        # Save
        self.save_to_file()

        return True

    # For main class to get data within class
    def get_flights(self):
        formatted_flights = []  # Initialize Var

        for flight in self.data:
            # Format the time and duration, omit next_day
            formatted_flight = {
                "origin": flight["origin"],
                "destination": flight["destination"],
                "flight_number": flight["flight_number"],
                "departure": self.format_time(flight["departure"]),
                "arrival": self.format_time(flight["arrival"]),
                "duration": self.calculate_duration(
                    flight["departure"], flight["arrival"], flight["next_day"]
                ),
            }
            # Add symbol for next day flights
            if flight["next_day"] == "Y":
                formatted_flight["arrival"] = "+" + formatted_flight["arrival"]

            # Add the data
            formatted_flights.append(formatted_flight)
        return formatted_flights

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=2)

    # Generic function to sanity check inputted times
    @staticmethod
    def is_valid_time(time_str):
        try:
            int(time_str[:2])
            int(time_str[2:])
            return True
        except ValueError:
            return False

    # Generic function to sanity check inputted times
    @staticmethod
    def format_time(time_str):
        hours = int(time_str[:2])
        minutes = int(time_str[2:])
        if hours != 12:
            hours = hours % 12

        return f'{(hours)}:{minutes:02}{("am" if hours < 12 else "pm")}'

    # Handle the calculation of next or same day flight durations
    @staticmethod
    def calculate_duration(departure, arrival, next_day):
        # Assume departure and arrival are in HHMM format
        departure_minutes = int(departure[:2]) * 60 + int(departure[2:])
        arrival_minutes = int(arrival[:2]) * 60 + int(arrival[2:])

        if next_day.upper() == "Y":
            arrival_minutes += 24 * 60  # Add 24 hours if arrival is on the next day

        duration_minutes = arrival_minutes - departure_minutes
        hours, minutes = divmod(duration_minutes, 60)
        return f"{hours}:{minutes:02}"
