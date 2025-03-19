from process import get_flight_data

def edf_scheduling():
    """Implements Earliest Deadline First scheduling and returns flight details."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["departure"])  # Sort by earliest departure time (deadline)

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return results for GUI
