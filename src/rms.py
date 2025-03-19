def rms_scheduling(flights):
    """Schedule flights using Rate Monotonic Scheduling (RMS)."""
    flights.sort(key=lambda x: x['period'])  # Sort by smallest period (higher frequency)
    time = 0
    schedule = []
    
    for flight in flights:
        start_time = max(time, flight['arrival_time'])
        finish_time = start_time + flight['processing_time']
        schedule.append({
            'flight_id': flight['flight_id'],
            'start_time': start_time,
            'finish_time': finish_time
        })
        time = finish_time
    
    return schedule
