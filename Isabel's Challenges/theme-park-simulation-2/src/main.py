import pandas as pd
import numpy as np
from theme_park import ThemePark

def load_ride_info(file_path):
    return pd.read_csv(file_path)

def load_ride_transitions(file_path):
    return pd.read_csv(file_path, index_col=0)

def load_arrival_rates(file_path):
    return pd.read_csv(file_path)

def main():
    # Initialize an empty CSV file with column labels
    output_file = 'simulations_output.csv'
    pd.DataFrame(columns=['customer_id', 'n_rides', 'waiting_time', 'ride_time', 'arrival_rate', 'day', 'week']).to_csv(output_file, index=False)

    # Load data from CSV files
    ride_info = load_ride_info('data/ride_info.csv')
    ride_transitions = load_ride_transitions('data/ride_transitions.csv')
    arrival_rates = load_arrival_rates('data/arrival_rates.csv')

    # Convert ride_transitions to a numpy array and normalize it
    transition_matrix = ride_transitions.to_numpy()
    transition_matrix = transition_matrix / transition_matrix.sum(axis=1, keepdims=True)

    # Print column names for debugging
    print("Arrival Rates Columns:", arrival_rates.columns)

    # Check for required columns and provide default values if missing
    if 'day' not in arrival_rates.columns:
        arrival_rates['day'] = 'Unknown'
    if 'week' not in arrival_rates.columns:
        arrival_rates['week'] = 0

    # Run the simulation for each arrival rate
    for index, row in arrival_rates.iterrows():
        arrival_rate = row['arrival_rate']
        day = row['day']
        week_id = row['week']
        theme_park = ThemePark(ride_info, arrival_rate, transition_matrix)
        theme_park.simulate(max_attempts=10, arrival_rate=arrival_rate, day=day, week_id=week_id)

        # Append simulation data to the CSV file
        df = pd.DataFrame(theme_park.simulation_data)
        df.to_csv(output_file, mode='a', header=False, index=False)

        # Clear the nested array for the next day
        theme_park.simulation_data.clear()

if __name__ == "__main__":
    main()