import os
from src.fcfs import fcfs_schedule
from src.edf import edf_schedule
from src.mfq import mfq_schedule
from src.priority import priority_schedule
from src.rms import rms_schedule
from src.rr import rr_schedule
from src.sjf import sjf_schedule
from src.gui import SchedulerGUI

def main():
    print("Flight Ticket Pricing Optimization - Scheduler Selection")
    print("1. First-Come, First-Served (FCFS)")
    print("2. Earliest Deadline First (EDF)")
    print("3. Multi-Level Feedback Queue (MFQ)")
    print("4. Priority Scheduling")
    print("5. Rate Monotonic Scheduling (RMS)")
    print("6. Round Robin (RR)")
    print("7. Shortest Job First (SJF)")
    choice = int(input("Choose a scheduling algorithm (1-7): "))

    flights = [
        {"flight": "A101", "arrival": 0, "duration": 3, "priority": 2, "deadline": 5},
        {"flight": "B202", "arrival": 2, "duration": 6, "priority": 1, "deadline": 10},
        {"flight": "C303", "arrival": 4, "duration": 4, "priority": 3, "deadline": 8},
    ]

    if choice == 1:
        schedule = fcfs_schedule(flights)
    elif choice == 2:
        schedule = edf_schedule(flights)
    elif choice == 3:
        schedule = mfq_schedule(flights)
    elif choice == 4:
        schedule = priority_schedule(flights)
    elif choice == 5:
        schedule = rms_schedule(flights)
    elif choice == 6:
        schedule = rr_schedule(flights, quantum=2)
    elif choice == 7:
        schedule = sjf_schedule(flights)
    else:
        print("Invalid choice.")
        return
    
    print("\nOptimized Flight Schedule:")
    for flight in schedule:
        print(flight)

    root = SchedulerGUI(schedule)
    root.mainloop()

if __name__ == "__main__":
    main()
