from process import get_flight_data

def priority_scheduling():
    """Implements Priority Scheduling (based on lower price as higher priority)."""
    flights = get_flight_data()
    flights.sort(key=lambda x: x["price"])  # Lower price = Higher priority

    schedule = []
    for flight in flights:
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']}"
        )
    
    return schedule  # ✅ Return results for GUI
