def rr_scheduling(flights, quantum=2):
    print("Running RR Scheduling with quantum =", quantum)
    queue = flights[:]
    while queue:
        flight = queue.pop(0)
        print(f"Flight {flight['id']} executed for {quantum} time units.")
        flight["duration"] -= quantum
        if flight["duration"] > 0:
            queue.append(flight)

