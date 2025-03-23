import numpy as np
import matplotlib.pyplot as plt

# Define lanes
lanes = ["North", "South", "East", "West"]

# Function to simulate random vehicle arrivals
def generate_traffic():
    return {lane: np.random.randint(1, 20) for lane in lanes}  # Generates vehicles for each lane

# Generate traffic data for 5 cycles
traffic_samples = [generate_traffic() for _ in range(5)]

# Extract traffic data for each lane
north_traffic = [t["North"] for t in traffic_samples]
south_traffic = [t["South"] for t in traffic_samples]
east_traffic = [t["East"] for t in traffic_samples]
west_traffic = [t["West"] for t in traffic_samples]

# Plot traffic trends
plt.figure(figsize=(8, 5))
plt.plot(north_traffic, label="North", marker="o", linestyle="--")
plt.plot(south_traffic, label="South", marker="o", linestyle="--")
plt.plot(east_traffic, label="East", marker="o", linestyle="--")
plt.plot(west_traffic, label="West", marker="o", linestyle="--")

plt.xlabel("Time Cycle")
plt.ylabel("Number of Vehicles")
plt.title("Traffic Flow at Intersection")
plt.legend()
plt.grid(True)
plt.show()
