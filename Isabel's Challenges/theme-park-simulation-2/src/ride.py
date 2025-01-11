from collections import deque
import random

class Ride(deque):

    def __init__(self, ride_id, ride_name, ride_rate):
        """
        Initialize a Ride instance.

        :param ride_id: Unique identifier for the ride
        :param ride_name: Name of the ride
        :param ride_rate: Rate parameter for the exponential distribution of ride times
        """
        super().__init__()
        self.ride_id = ride_id
        self.ride_name = ride_name
        self.ride_rate = ride_rate
        self.customers_processed = 0
        self.total_ride_time = 0

    def add_customer(self, customer, arrival_time):
        """
        Add a customer to the ride's queue.

        :param customer: Customer object
        :param arrival_time: Time at which the customer arrives at the ride
        """
        self.append((customer, arrival_time))

    def carry_customer(self, current_time):
        """
        Process the next customer in the queue and calculate the completion time.

        :param current_time: Current time in the simulation
        :return: Tuple of (customer, completion_time)
        """
        if not self:
            raise IndexError("No customers in the queue.")

        customer, arrival_time = self.popleft()
        ride_time = random.expovariate(self.ride_rate)  # Generate ride time based on exponential distribution
        completion_time = current_time + ride_time

        # Update ride statistics
        self.customers_processed += 1
        self.total_ride_time += ride_time

        return customer, completion_time

    def __str__(self):
        """
        Return a string representation of the ride's queue.

        :return: String of customer IDs in the queue
        """
        return f"Ride {self.ride_name} Queue: {[customer.customer_id for customer, _ in self]}"