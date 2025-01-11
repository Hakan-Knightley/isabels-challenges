# Theme Park Simulation

## Overview
The Theme Park Simulation project models the movement of customers through a theme park, represented as a network of queues for various rides. The simulation captures customer arrivals, ride experiences, and transitions between rides, providing insights into customer behavior and ride utilization.

## Project Structure
```
theme-park-simulation
├── src
│   ├── main.py               # Entry point for the simulation
│   ├── priority_queue.py     # Implements the PriorityQueue class
│   ├── customer.py           # Defines the Customer class
│   ├── ride.py               # Implements the Ride class
│   ├── theme_park.py         # Defines the ThemePark class
│   └── utils
│       └── __init__.py       # Initialization file for utils package
├── data
│   ├── ride_info.csv         # Ride information (IDs, names, rates)
│   ├── ride_transitions.csv   # Transition probabilities between rides
│   └── arrival_rates.csv      # Customer arrival rates for simulations
├── requirements.txt           # Required packages for the project
└── README.md                  # Documentation for the project
```

## How to Run the Simulation
1. Ensure you have Python installed on your machine.
2. Install the required packages by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the simulation by executing the `main.py` file:
   ```
   python src/main.py
   ```

## Additional Information
- The simulation uses a priority queue to manage events, ensuring that customer arrivals and ride processing are handled in the correct order.
- Data for rides and customer arrival rates are loaded from CSV files located in the `data` directory.
- The project can be extended by adding more rides or modifying the transition probabilities in the `ride_transitions.csv` file. 

Feel free to explore the code and modify it to suit your needs!