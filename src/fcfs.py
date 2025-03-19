def fcfs_scheduling(flights):
    print("Running FCFS Scheduling...")
    flights.sort(key=lambda x: x["arrival"])  # Sort by arrival time
    for flight in flights:
        print(f"Flight {flight['id']} scheduled at arrival {flight['arrival']}.")
