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
    print(data)
    # if date not in data:
    #     return "No data available for the specified date."

    report = f"========================= DAILY REPORT ========================\n"
    report += f"Date Time Temperature Humidity Rainfall\n"
    report += f"==================== ======== =========== ======== ========\n"

    for key, value in data.items():
        print(f"key: {key} | value: {value}")
        if date in key[:8]:
            year = key[:4]
            month = int(key[4:6])
            day = int(key[6:8])
            time = key[8:9] + ":" + key[9:10] + ":" + key[10:11]
            month_name = calendar.month_name[month]

            temperature = value.get("t", "N/A")
            humidity = value.get("h", "N/A")
            rainfall = value.get("r", "N/A")

            report += f"{month_name} {day}, {year} {time} {temperature} {humidity} {rainfall}\n"

    return report


def report_historical(data=None):
    report = "Historical Weather Data:\n\n"
    for date in sorted(data.keys()):
        month = int(date[4:6])
        day = int(date[6:])
        month_name = calendar.month_name[month]
        max_temp = max_temperature(data, date)
        min_temp = min_temperature(data, date)
        max_hum = max_humidity(data, date)
        min_hum = min_humidity(data, date)
        rain = tot_rain(data, date)

        report += f"{month_name} {day}, {date[:4]}:\n"
        report += f"Maximum Temperature: {max_temp}°C\n"
        report += f"Minimum Temperature: {min_temp}°C\n"
        report += f"Maximum Humidity: {max_hum}%\n"
        report += f"Minimum Humidity: {min_hum}%\n"
        report += f"Total Rainfall: {rain} mm\n\n"

    return report
