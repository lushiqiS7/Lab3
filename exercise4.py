# Function to calculate the average temperature
def calc_average_temperature(temperature_list):
    if not temperature_list:
        return None  # Handle the case of an empty list
    else:
        average = sum(temperature_list) / len(temperature_list)
        return average

# Function to calculate the minimum and maximum temperature
def calc_min_max_temperature(temperature_list):
    if not temperature_list:
        return [None, None]  # Handle the case of an empty list
    else:
        min_temp = min(temperature_list)
        max_temp = max(temperature_list)
        return [min_temp, max_temp]