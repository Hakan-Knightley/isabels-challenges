class Customer:
    def __init__(self, customer_id, arrival_time):
        self.customer_id = customer_id
        self.arrival_time = arrival_time
        self.path = []  # Sequence of ride_ids the customer visits
        self.ride_times = []  # Time spent on each ride
        self.wait_times = []  # Time spent in each ride's queue

    def record_ride(self, ride_id, ride_time, wait_time):
        self.path.append(ride_id)
        self.ride_times.append(ride_time)
        self.wait_times.append(wait_time)