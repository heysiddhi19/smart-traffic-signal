import numpy as np

# Define lanes
lanes = ["North", "South", "East", "West"]

# Function to simulate random vehicle arrivals
def generate_traffic():
    return {lane: np.random.randint(1, 20) for lane in lanes}  # Generates vehicles for each lane

# Function to calculate optimized signal timing
def calculate_signal_time(traffic_data):
    base_time = 10  # Minimum green signal time (in seconds)
    max_time = 40   # Maximum green signal time (in seconds)
    total_cars = sum(traffic_data.values())  # Total number of vehicles at the intersection

    # If no cars at all, assign the base time to each lane
    if total_cars == 0:
        return {lane: base_time for lane in lanes}

    # Allocate time proportionally based on traffic count
    signal_times = {}
    for lane, cars in traffic_data.items():
        time_allocated = (cars / total_cars) * (max_time * len(lanes))  # Proportional time allocation
        signal_times[lane] = max(base_time, min(round(time_allocated, 2), max_time))  # Ensure min/max limits

    return signal_times

# Generate random traffic data
traffic_data = generate_traffic()

# Calculate optimized signal times
signal_times = calculate_signal_time(traffic_data)

# Display results
print("\n🚦 Optimized Signal Timings:")
for lane, time in signal_times.items():
    print(f"{lane}: {time} sec")
