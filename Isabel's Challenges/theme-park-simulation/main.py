import random
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, event):
        heapq.heappush(self.queue, event)

    def popleft(self):
        if not self.queue:
            raise IndexError("pop from an empty priority queue")
        return heapq.heappop(self.queue)

class Customer:
    def __init__(self, customer_id, arrival_time):
        self.customer_id = customer_id
        self.arrival_time = arrival_time
        self.path = []
        self.ride_times = []
        self.wait_times = []

    def record_ride(self, ride_id, ride_time, wait_time):
        self.path.append(ride_id)
        self.ride_times.append(ride_time)
        self.wait_times.append(wait_time)

class Ride:
    def __init__(self, ride_id, ride_name, ride_rate):
        self.ride_id = ride_id
        self.ride_name = ride_name
        self.ride_rate = ride_rate
        self.customers_processed = 0
        self.total_ride_time = 0

    def generate_ride_time(self):
        return random.expovariate(1 / self.ride_rate)

    def carry_customer(self, customer, current_time):
        ride_time = self.generate_ride_time()
        self.customers_processed += 1
        self.total_ride_time += ride_time
        return customer, current_time + ride_time

    def __str__(self):
        return f"Ride {self.ride_id}: {self.ride_name}"

def main():
    # Initialize rides and customers
    rides = [
        Ride(1, "Ferris Wheel", 5.0),
        Ride(2, "Roller Coaster", 10.0),
        Ride(3, "Haunted House", 7.5)
    ]
    
    customers = [
        Customer(1, 0),
        Customer(2, 1),
        Customer(3, 2)
    ]
    
    # Initialize the priority queue for managing ride events
    event_queue = PriorityQueue()
    
    # Simulate customer arrivals and ride experiences
    for customer in customers:
        for ride in rides:
            # Simulate the customer going on a ride
            ride_time = ride.generate_ride_time()
            customer.record_ride(ride.ride_id, ride_time, 0)  # Assuming wait time is 0 for simplicity
            event_queue.push((customer.arrival_time + ride_time, ride.ride_id))
    
    # Process events in the queue
    while event_queue.queue:
        event_time, ride_id = event_queue.popleft()
        print(f"At time {event_time}, ride {ride_id} is being processed.")

if __name__ == "__main__":
    main()