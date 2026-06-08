import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import csv

#Connect to ESP32
ser = serial.Serial('COM3', 9600, timeout=1)
ser.flushInput()


# Create log file with timestamp in name
log_filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Write header to CSV
with open(log_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Voltage'])

# Storage for live plot
voltages = []
threshold = 12.2

fig, ax = plt.subplots(figsize=(10,5))

def update(frame):
    line = ser.readline().decode('utf-8').strip()
    if line:
        voltage = float(line)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #Save to CSV
        with open(log_filename, 'a', newline ='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, voltage])

        # Update plot
        voltages.append(voltage)
        ax.clear()
        ax.plot(voltages, marker='o', color='blue', label='Voltage')
        ax.axhline(y=threshold, color='red', linestyle='--', label='Threshold')
        ax.set_title(f'Live Voltage Logger - Saving to {log_filename}')
        ax.set_xlabel('Reading Number')
        ax.set_ylabel('Voltage (V)')
        ax.legend()
        ax.grid(True)

anim = animation.FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
plt.show()