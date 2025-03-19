import tkinter as tk
from fcfs import fcfs_scheduling
from edf import edf_scheduling
from mfq import mfq_scheduling
from priority import priority_scheduling
from rms import rms_scheduling
from rr import rr_scheduling
from sjf import sjf_scheduling

# Dictionary mapping scheduling algorithms to their functions
scheduler_functions = {
    "FCFS": fcfs_scheduling,
    "EDF": edf_scheduling,
    "MFQ": mfq_scheduling,
    "Priority": priority_scheduling,
    "RMS": rms_scheduling,
    "Round Robin": rr_scheduling,
    "SJF": sjf_scheduling
}

def run_selected_scheduler():
    """Runs the selected scheduling algorithm and displays the results in the UI."""
    algorithm = algo_var.get()  # Get the selected algorithm
    if algorithm in scheduler_functions:
        results = scheduler_functions[algorithm]()  # Run the selected algorithm
        
        # Clear previous results
        result_text.delete("1.0", tk.END)
        
        # Display results
        for line in results:
            result_text.insert(tk.END, line + "\n")

# GUI setup
root = tk.Tk()
root.title("Flight Ticket Pricing Optimization")

# Dropdown for selecting the algorithm
algo_var = tk.StringVar()
algo_var.set("FCFS")  # Default selection
algo_menu = tk.OptionMenu(root, algo_var, *scheduler_functions.keys())
algo_menu.pack()

# Run button
run_button = tk.Button(root, text="Run Scheduler", command=run_selected_scheduler)
run_button.pack()

# Text area to display results
result_text = tk.Text(root, height=15, width=80)
result_text.pack()

root.mainloop()
