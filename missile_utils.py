def calculate_travel_time(range_km, speed_mach):
    speed_kmh = speed_mach * 1225  # approx speed of sound in km/h
    return range_km / speed_kmh

def format_time(hours):
    minutes = hours * 60
    return f"{minutes:.2f} minutes"
