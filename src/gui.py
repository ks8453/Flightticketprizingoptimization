import tkinter as tk
from tkinter import ttk
import sys

# Ensure Python can find the scheduler files
sys.path.append("src")

# Import scheduling algorithms
from fcfs import fcfs_scheduling
from edf import edf_scheduling
from mfq import mfq_scheduling
from priority import priority_scheduling
from rms import rms_scheduling
from rr import rr_scheduling
from sjf import sjf_scheduling

class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Pricing Optimization")

        # Dropdown menu for scheduling selection
        self.label = tk.Label(root, text="Choose a Scheduling Algorithm:")
        self.label.pack(pady=10)

        self.scheduling_options = [
            "FCFS", "EDF", "MFQ", "Priority", "RMS", "RR", "SJF"
        ]
        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set(self.scheduling_options[0])  # Default selection

        self.dropdown = ttk.Combobox(root, textvariable=self.selected_algorithm, values=self.scheduling_options)
        self.dropdown.pack(pady=5)

        # Button to start the selected scheduling algorithm
        self.run_button = tk.Button(root, text="Run Scheduler", command=self.run_selected_scheduler)
        self.run_button.pack(pady=10)

        # Output Label
        self.output_label = tk.Label(root, text="", fg="blue")
        self.output_label.pack(pady=5)

    def get_flights_data(self):
        """Simulates flight data for scheduling."""
        return [
            {"id": 1, "arrival": 3, "duration": 5, "priority": 2},
            {"id": 2, "arrival": 1, "duration": 3, "priority": 1},
            {"id": 3, "arrival": 2, "duration": 2, "priority": 3}
        ]

    def run_selected_scheduler(self):
        """Runs the selected scheduler with flight data."""
        algorithm = self.selected_algorithm.get()
        flights = self.get_flights_data()

        # Mapping of scheduler functions
        scheduler_functions = {
            "FCFS": fcfs_scheduling,
            "EDF": edf_scheduling,
            "MFQ": mfq_scheduling,
            "Priority": priority_scheduling,
            "RMS": rms_scheduling,
            "RR": rr_scheduling,
            "SJF": sjf_scheduling
        }

        if algorithm in scheduler_functions:
            self.output_label.config(text=f"Running {algorithm} Scheduling...")
            scheduler_functions[algorithm](flights)  # ✅ Pass the required argument
        else:
            self.output_label.config(text="Invalid Selection")

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()

