def mfq_scheduling(flights):
    print("Running MFQ Scheduling...")
    flights.sort(key=lambda x: x["priority"])  # Assume priority levels
    for flight in flights:
        print(f"Flight {flight['id']} scheduled with priority {flight['priority']}.")
