def edf_scheduling(flights):
    print("Running EDF Scheduling...")
    flights.sort(key=lambda x: x["arrival"])  # Assume arrival time as deadline
    for flight in flights:
        print(f"Flight {flight['id']} scheduled with deadline {flight['arrival']}.")
