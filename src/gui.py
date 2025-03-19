import tkinter as tk
from tkinter import ttk, messagebox
from src.process import TicketScheduler

class FlightPricingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Ticket Pricing Optimization")
        self.root.geometry("500x400")

        self.scheduler = TicketScheduler()

        # Dropdown for scheduler selection
        self.label_scheduler = tk.Label(root, text="Select Scheduling Algorithm:")
        self.label_scheduler.pack(pady=5)

        self.scheduler_options = ["FCFS", "EDF", "MFQ", "Priority", "RMS", "RR", "SJF"]
        self.scheduler_var = tk.StringVar()
        self.scheduler_dropdown = ttk.Combobox(root, textvariable=self.scheduler_var, values=self.scheduler_options)
        self.scheduler_dropdown.pack(pady=5)
        self.scheduler_dropdown.current(0)

        # Button to calculate ticket price
        self.button_calculate = tk.Button(root, text="Calculate Ticket Prices", command=self.calculate_prices)
        self.button_calculate.pack(pady=20)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def calculate_prices(self):
        selected_scheduler = self.scheduler_var.get()
        result = self.scheduler.calculate_price(selected_scheduler)
        self.result_label.config(text=f"Calculated Price: ${result}")
        messagebox.showinfo("Price Calculation", f"Final ticket price: ${result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlightPricingGUI(root)
    root.mainloop()

