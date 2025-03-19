import random

class TicketScheduler:
    def __init__(self):
        pass

    def calculate_price(self, algorithm):
        if algorithm == "FCFS":
            return self.fcfs()
        elif algorithm == "EDF":
            return self.edf()
        elif algorithm == "MFQ":
            return self.mfq()
        elif algorithm == "Priority":
            return self.priority()
        elif algorithm == "RMS":
            return self.rms()
        elif algorithm == "RR":
            return self.rr()
        elif algorithm == "SJF":
            return self.sjf()
        else:
            return "Invalid Algorithm"

    def fcfs(self):
        return round(random.uniform(100, 500), 2)

    def edf(self):
        return round(random.uniform(120, 480), 2)

    def mfq(self):
        return round(random.uniform(90, 470), 2)

    def priority(self):
        return round(random.uniform(130, 450), 2)

    def rms(self):
        return round(random.uniform(110, 490), 2)

    def rr(self):
        return round(random.uniform(105, 460), 2)

    def sjf(self):
        return round(random.uniform(95, 430), 2)

