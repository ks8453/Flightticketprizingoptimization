def rms_scheduling(flights):
    print("Running RMS Scheduling...")
    flights.sort(key=lambda x: x["duration"])  # Shortest period first
    for flight in flights:
        print(f"Flight {flight['id']} scheduled with duration {flight['duration']}.")
