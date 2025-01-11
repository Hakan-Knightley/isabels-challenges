import pandas as pd
import numpy as np
from priority_queue import PriorityQueue
from customer import Customer
from ride import Ride

class ThemePark:
    def __init__(self, rides, arrival_rate, transition_matrix):
        self.rides = rides
        self.arrival_rate = arrival_rate
        self.transition_matrix = transition_matrix
        self.event_queue = PriorityQueue()
        self.customers = []
        self.simulation_data = []  # List to store simulation data

    def route_customer(self, current_ride_id):
        probabilities = self.transition_matrix[current_ride_id]
        next_ride_id = np.random.choice(len(probabilities), p=probabilities)
        return next_ride_id

    def simulate(self, max_attempts, arrival_rate, day, week_id, verbose=False):
        current_time = 0
        customer_id = 1  # Start customer_id from 1

        # Schedule the first customer arrival
        self.event_queue.push(np.random.exponential(1 / arrival_rate), 0)

        attempts = 0
        while self.event_queue.queue and attempts < max_attempts:
            event_time, ride_id = self.event_queue.popleft()
            current_time = event_time

            if ride_id == 0:  # New customer arrival
                customer = Customer(customer_id, current_time)
                self.customers.append(customer)
                customer_id += 1

                # Route customer to the first ride
                next_ride_id = self.route_customer(0)
                self.event_queue.push(current_time, next_ride_id)

                # Schedule the next customer arrival
                next_arrival_time = current_time + np.random.exponential(1 / arrival_rate)
                self.event_queue.push(next_arrival_time, 0)

                if verbose:
                    print(f"Customer {customer.customer_id} arrived at time {current_time}")

                attempts += 1

            else:  # Customer being processed by a ride
                ride = self.rides.iloc[ride_id - 1]
                ride_time = np.random.exponential(ride['ride_rate'])
                wait_time = len(self.event_queue.queue) * ride_time

                customer = self.customers[-1]
                customer.record_ride(ride_id, ride_time, wait_time)

                self.simulation_data.append({
                    'customer_id': customer.customer_id,
                    'n_rides': len(customer.path),
                    'waiting_time': sum(customer.wait_times),
                    'ride_time': sum(customer.ride_times),
                    'arrival_rate': arrival_rate,
                    'day': day,
                    'week': week_id
                })

                # Route customer to the next ride or exit
                next_ride_id = self.route_customer(ride_id)
                self.event_queue.push(current_time + ride_time, next_ride_id)

        # Combine data for the same customer ID
        combined_data = {}
        for customer in self.customers:
            customer_id = customer.customer_id
            if customer_id not in combined_data:
                combined_data[customer_id] = {
                    'customer_id': customer_id,
                    'n_rides': len(customer.path),
                    'waiting_time': sum(customer.wait_times),
                    'ride_time': sum(customer.ride_times),
                    'arrival_rate': arrival_rate,
                    'day': day,
                    'week': week_id
                }
            else:
                combined_data[customer_id]['n_rides'] += len(customer.path)
                combined_data[customer_id]['waiting_time'] += sum(customer.wait_times)
                combined_data[customer_id]['ride_time'] += sum(customer.ride_times)

        self.simulation_data = list(combined_data.values())

    def __str__(self):
        status = ""
        for ride in self.rides:
            status += str(ride) + "\n"
        return status