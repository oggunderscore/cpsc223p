import json


class Flights:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        try:
            with open(filename, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass

    def add_flight(
        self, origin, destination, flight_number, departure, next_day, arrival
    ):
        if not self.is_valid_time(departure) or not self.is_valid_time(arrival):
            return False

        flight_data = {
            "origin": origin,
            "destination": destination,
            "flight_number": flight_number,
            "departure": departure,
            "next_day": next_day,
            "arrival": arrival,
        }

        self.data.append(flight_data)
        self.save_to_file()
        return True

    def get_flights(self):
        formatted_flights = []
        for flight in self.data:
            formatted_flight = {
                "origin": flight["origin"],
                "destination": flight["destination"],
                "flight_number": flight["flight_number"],
                "departure": self.format_time(flight["departure"]),
                "arrival": self.format_time(flight["arrival"]),
                "duration": self.calculate_duration(
                    flight["departure"], flight["arrival"]
                ),
            }
            formatted_flights.append(formatted_flight)
        return formatted_flights

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=2)

    @staticmethod
    def is_valid_time(time_str):
        try:
            int(time_str[:2])
            int(time_str[2:])
            return True
        except ValueError:
            return False

    @staticmethod
    def format_time(time_str):
        hours = int(time_str[:2])
        minutes = int(time_str[2:])
        return f'{hours % 12}:{minutes:02}{("am" if hours < 12 else "pm")}'

    @staticmethod
    def calculate_duration(departure, arrival):
        # Assume departure and arrival are in HHMM format
        departure_minutes = int(departure[:2]) * 60 + int(departure[2:])
        arrival_minutes = int(arrival[:2]) * 60 + int(arrival[2:])
        duration_minutes = arrival_minutes - departure_minutes
        hours, minutes = divmod(duration_minutes, 60)
        return f"{hours}:{minutes:02}"
