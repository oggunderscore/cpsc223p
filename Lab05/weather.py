import json
import calendar

def read_data(filename = None):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def write_data(data = None, filename = None):
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(data = None, date = None):
    max_temp = float('-inf')        # Maybe set this to none / 0?
    for key, value in data.items():
        if date in key and 't' in value:
            max_temp = max(max_temp, value['t'])
    return max_temp

def min_temperature(data = None, date = None):
    min_temp = float('inf')         # Maybe set this to none / 0?
    for key, value in data.items():
        if date in key and 't' in value:
            min_temp = min(min_temp, value['t'])
    return min_temp

def max_humidity(data = None, date = None):
    max_hum = 0
    for key, value in data.items():
        if date in key and 'h' in value:
            max_hum = max(max_hum, value['h'])
    return max_hum

def min_humidity(data = None, date = None):
    min_hum = 100
    for key, value in data.items():
        if date in key and 'h' in value:
            min_hum = min(min_hum, value['h'])
    return min_hum

def tot_rain(data = None, date = None):
    total_rain = 0
    for key, value in data.items():
        if date in key and 'r' in value:
            total_rain += value['r']
    return total_rain

def report_daily(data = None, date = None):
    month = int(date[4:6])
    day = int(date[6:])
    month_name = calendar.month_name[month]
    max_temp = max_temperature(data, date)
    min_temp = min_temperature(data, date)
    max_hum = max_humidity(data, date)
    min_hum = min_humidity(data, date)
    rain = tot_rain(data, date)

    report = f"Weather Report for {month_name} {day}, {date[:4]}:\n"
    report += f"Maximum Temperature: {max_temp}°C\n"
    report += f"Minimum Temperature: {min_temp}°C\n"
    report += f"Maximum Humidity: {max_hum}%\n"
    report += f"Minimum Humidity: {min_hum}%\n"
    report += f"Total Rainfall: {rain} mm\n"

    return report

def report_historical(data = None):
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
