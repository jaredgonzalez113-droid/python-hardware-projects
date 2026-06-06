import matplotlib.pyplot as plt
from datetime import datetime

# Read voltage readings and timestamps from file
timestamps = []
voltages = []

with open("readings.csv", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
        voltage = float(parts[1])
        timestamps.append(timestamp)
        voltages.append(voltage)

# Calculate statistics
average = sum(voltages) / len(voltages)
max_voltage = max(voltages)
min_voltage = min(voltages)
voltages_range = max_voltage - min_voltage

# Display results
print(f"Readings: {voltages}")
print(f"Average voltage: {average:.2f}V" )
print(f"Max: {max_voltage:.2f}V")
print(f"Min: {min_voltage:.2f}V")
print(f"Range: {voltages_range:.2f}V")

# Check threshold
threshold = 12.2
for voltage in voltages:
    if voltage > threshold:
        print(f"{voltage}V - Above threshold")
    else:
        print(f"{voltage}V - OK")

#Count how many readings are above threshold
number_above_threshold = sum(1 for voltage in voltages if voltage > threshold)
total_readings = len(voltages)
print(f"{number_above_threshold} readings above threshold out of {total_readings}")

#Plot the readings
plt.figure(figsize=(10, 5))
plt.plot(timestamps, voltages, marker='o', color='blue', label='Voltage')
plt.axhline(y=threshold, color ='red', linestyle='--', label='Threshold')
plt.title('Voltage Readings Over Time')
plt.xlabel('Time')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
