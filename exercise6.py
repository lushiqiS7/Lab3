# Function to calculate the median temperature from a list of floats
def calc_median_temperature(temperature_list):
    if not temperature_list:
        return None  # Handle the case of an empty list
    else:
        sorted_temperatures = sorted(temperature_list)
        n = len(sorted_temperatures)
        if n % 2 == 1:
            median = sorted_temperatures[n // 2]
        else:
            median = (sorted_temperatures[n // 2 - 1] + sorted_temperatures[n // 2]) / 2
        return median