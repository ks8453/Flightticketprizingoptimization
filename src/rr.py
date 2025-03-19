from collections import deque

def rr_scheduling(flights, time_quantum=5):
    """Schedule flights using Round Robin (RR)."""
    queue = deque(flights)
    time = 0
    schedule = []
    
    while queue:
        flight = queue.popleft()
        start_time = max(time, flight['arrival_time'])
        execution_time = min(flight['processing_time'], time_quantum)
        finish_time = start_time + execution_time
        
        schedule.append({
            'flight_id': flight['flight_id'],
            'start_time': start_time,
            'finish_time': finish_time
        })
        
        time = finish_time
        remaining_time = flight['processing_time'] - execution_time
        if remaining_time > 0:
            flight['processing_time'] = remaining_time
            queue.append(flight)  # Re-add to queue if not finished
    
    return schedule
