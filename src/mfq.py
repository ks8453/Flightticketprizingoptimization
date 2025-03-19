from process import get_flight_data

def mfq_scheduling():
    """Implements Multi-Level Feedback Queue scheduling and returns flight details."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["price"])  # Simulating priority based on price (cheaper flights first)

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return results for GUI
