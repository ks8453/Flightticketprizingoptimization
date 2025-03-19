def edf_scheduling(flights):
    """Schedule flights using Earliest Deadline First (EDF)."""
    flights.sort(key=lambda x: x['deadline'])  # Sort by earliest deadline
    time = 0
    schedule = []
    
    for flight in flights:
        start_time = max(time, flight['arrival_time'])
        finish_time = start_time + flight['processing_time']
        if finish_time <= flight['deadline']:  # Only schedule if it meets the deadline
            schedule.append({
                'flight_id': flight['flight_id'],
                'start_time': start_time,
                'finish_time': finish_time
            })
            time = finish_time
    
    return schedule
