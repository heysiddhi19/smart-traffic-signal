import numpy as np
import time

# Define lanes
lanes = ["North", "South", "East", "West"]

# Simulate random vehicle arrivals per second
def generate_traffic():
    return {lane: np.random.randint(1, 10) for lane in lanes}

# Run simulation for 5 cycles
for cycle in range(5):
    traffic_data = generate_traffic()
    print(f"Cycle {cycle+1}: {traffic_data}")
    time.sleep(1)  # Simulating real-time updates
