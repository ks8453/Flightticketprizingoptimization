def priority_scheduling(flights):
    print("Running Priority Scheduling...")
    flights.sort(key=lambda x: x["priority"])  # Sort by priority
    for flight in flights:
        print(f"Flight {flight['id']} scheduled with priority {flight['priority']}.")
