# Read voltage readings from file
voltages = []

with open("readings.csv", "r") as file:
    for line in file:
        voltage = float(line.strip())
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

