from process import get_flight_data

def sjf_scheduling():
    """Implements Shortest Job First scheduling and returns flight details."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["departure"] - x["arrival"])  # Shortest flight time first

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return results for GUI
