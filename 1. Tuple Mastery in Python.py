
# 1. Tuple Mastery in Python

def format_itineraries(flight_list):
    result = ""
    for i, flight in enumerate(flight_list, 1): 
        traveler_name, origin, destination = flight
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result.strip()

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
itinerary_string = format_itineraries(flights)
print(itinerary_string)