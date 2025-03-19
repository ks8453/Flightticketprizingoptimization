from process import get_flight_data

def rr_scheduling(time_quantum=2):
    """Implements Round Robin scheduling and returns flight details."""
    flights = get_flight_data()
    queue = flights[:]  # Copy of flights list
    schedule = []
    
    time = 0
    while queue:
        flight = queue.pop(0)
        schedule.append(
            f"Flight {flight['id']} ({flight['name']}) to {flight['destination']} - "
            f"Arrival: {flight['arrival']} | Departure: {flight['departure']} | Price: ${flight['price']} | Processed at time {time}"
        )
        time += time_quantum  # Simulate quantum time
    
    return schedule  # ✅ Return results for GUI
