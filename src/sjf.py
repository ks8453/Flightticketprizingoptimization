def sjf_scheduling(flights):
    print("Running SJF Scheduling...")
    flights.sort(key=lambda x: x["duration"])  # Sort by shortest duration
    for flight in flights:
        print(f"Flight {flight['id']} scheduled with duration {flight['duration']}.")
