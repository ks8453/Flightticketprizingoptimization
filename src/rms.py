from process import get_flight_data

def rms_scheduling():
    """Implements Rate-Monotonic Scheduling (shortest period flights first)."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["departure"] - x["arrival"])  # Shorter flight duration first

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return results for GUI
