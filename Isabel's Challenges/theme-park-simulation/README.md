# Theme Park Simulation

This project simulates a theme park experience, managing customer queues and ride times through a series of classes. The simulation includes customers visiting various rides, tracking their wait times and ride durations.

## Project Structure

```
theme-park-simulation
├── src
│   ├── __init__.py
│   ├── customer.py
│   ├── ride.py
│   ├── priority_queue.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Classes

- **Customer**: Represents a customer in the theme park with attributes for customer ID, arrival time, rides visited, ride times, and wait times. It includes methods to record rides.

- **Ride**: Represents a ride in the theme park with attributes for ride ID, name, rate, number of customers processed, and total ride time. It includes methods to carry customers and generate ride times.

- **PriorityQueue**: Implements a priority queue to manage events in the simulation, allowing for efficient handling of customer arrivals and ride processing.

## Requirements

To run this simulation, ensure you have the necessary dependencies listed in `requirements.txt`. You can install them using:

```
pip install -r requirements.txt
```

## Running the Simulation

To start the simulation, run the `main.py` file:

```
python src/main.py
```

## Additional Notes

This simulation can be extended with additional features such as different types of rides, varying customer behaviors, and more complex queue management strategies.