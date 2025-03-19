import random

def get_flight_data():
    """Returns a list of sample flights with names, arrival & departure times, and random prices."""
    destinations = ["New York", "London", "Tokyo", "Paris", "Dubai"]
    
    flights = [
        {"id": 1, "name": "Flight A", "arrival": 3, "departure": 8},
        {"id": 2, "name": "Flight B", "arrival": 1, "departure": 4},
        {"id": 3, "name": "Flight C", "arrival": 2, "departure": 6},
        {"id": 4, "name": "Flight D", "arrival": 5, "departure": 9},
        {"id": 5, "name": "Flight E", "arrival": 4, "departure": 7}
    ]

    # Assign random price and destination
    for flight in flights:
        flight["price"] = random.randint(100, 1000)  # Generate a random price
        flight["destination"] = random.choice(destinations)  # Random destination

    return flights
