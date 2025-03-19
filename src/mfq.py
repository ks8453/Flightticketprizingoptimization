from collections import deque

def mfq_scheduling(flights, time_quantum=[3, 6, 12]):
    """Schedule flights using Multi-Level Feedback Queue (MFQ)."""
    queues = [deque() for _ in range(len(time_quantum))]
    time = 0
    schedule = []
    
    for flight in flights:
        queues[0].append(flight)  # Initially put all flights in the first queue
    
    while any(queues):
        for level, q in enumerate(queues):
            if q:
                flight = q.popleft()
                start_time = max(time, flight['arrival_time'])
                execution_time = min(flight['processing_time'], time_quantum[level])
                finish_time = start_time + execution_time
                
                schedule.append({
                    'flight_id': flight['flight_id'],
                    'start_time': start_time,
                    'finish_time': finish_time
                })
                
                time = finish_time
                
                remaining_time = flight['processing_time'] - execution_time
                if remaining_time > 0 and level < len(time_quantum) - 1:
                    flight['processing_time'] = remaining_time
                    queues[level + 1].append(flight)  # Move to the next queue
    
    return schedule
