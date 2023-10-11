import json
import calendar


def read_data(filename=None):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}


def write_data(data=None, filename=None):
    with open(filename, "w") as file:
        json.dump(data, file)


def max_temperature(data=None, date=None):
    max_temp = 0
    for key, value in data.items():
        if date in key and "t" in value:
            max_temp = max(max_temp, value["t"])
    return max_temp


def min_temperature(data=None, date=None):
    min_temp = 0
    for key, value in data.items():
        if date in key and "t" in value:
            min_temp = min(min_temp, value["t"])
    return min_temp


def max_humidity(data=None, date=None):
    max_hum = 0
    for key, value in data.items():
        if date in key and "h" in value:
            max_hum = max(max_hum, value["h"])
    return max_hum


def min_humidity(data=None, date=None):
    min_hum = 100
    for key, value in data.items():
        if date in key and "h" in value:
            min_hum = min(min_hum, value["h"])
    return min_hum


def tot_rain(data=None, date=None):
    total_rain = 0
    for key, value in data.items():
        if date in key and "r" in value:
            total_rain += value["r"]
    return total_rain


def report_daily(data=None, date=None):
    report = f"========================= DAILY REPORT ========================\n"
    report += f"{('Date'):24} Time Temperature Humidity Rainfall\n"
    report += f"==================== ======== =========== ======== ========\n"
    has_data = False
    for key, value in data.items():
        if date in key[:8]:
            has_data = True
            year = key[:4]
            month = int(key[4:6])
            day = str(key[6:8])
            time = key[8:10] + ":" + key[10:12] + ":" + key[12:14]
            month_name = calendar.month_name[month]
            date_string = month_name + " " + day + ", " + year

            temperature = value.get("t", "N/A")
            humidity = value.get("h", "N/A")
            rainfall = value.get("r", "N/A")

            report += f"{date_string:20} {time:8} {temperature:11} {humidity:8} {rainfall:8}\n"
    if has_data == False:
        return "\nNo data available for the specified date."
    return report


def report_historical(data=None):
    if len(data) == 0:
        return "\nNo data available."

    report = f"\n========================= HISTORICAL REPORT ========================\n"
    report += f"{(' '):15} Minimum    Maximum    Minimum    Maximum    Total\n"
    report += f"{('Date'):24} Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    report += (
        f"==================== =========== =========== ======== ======== ========\n"
    )

    # Initialize variables for temperature and humidity range
    min_temp = float("inf")
    max_temp = float("-inf")
    min_hum = 100
    max_hum = 0
    total_rain = 0.0

    for key, value in data.items():
        year = key[:4]
        month = int(key[4:6])
        day = str(key[6:8])
        month_name = calendar.month_name[month]
        date_string = month_name + " " + day + ", " + year

        temperature = value.get("t", "N/A")
        humidity = value.get("h", "N/A")
        rainfall = value.get("r", "N/A")

        # Update temperature and humidity range
        if temperature != "N/A":
            min_temp = min(min_temp, temperature)
            max_temp = max(max_temp, temperature)
        if humidity != "N/A":
            min_hum = min(min_hum, humidity)
            max_hum = max(max_hum, humidity)

        # Update total rainfall
        if rainfall != "N/A":
            total_rain += rainfall

        report += f"{date_string:19}  {min_temp:11} {max_temp:11} {min_hum:8} {max_hum:8} {round(total_rain, 1):8}\n"

    return report
