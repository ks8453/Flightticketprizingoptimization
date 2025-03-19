from process import get_flight_data

def fcfs_scheduling():
    """Implements FCFS scheduling and returns flight details."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["arrival"])  # Sort by arrival time

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return the schedule for GUI
