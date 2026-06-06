import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

# Connect to EPS32
ser = serial.Serial('COM3', 9600, timeout=1)

#Storage for live data
timestamps = []
voltages = []
threshold = 12.2

#Setup up the plot
fig, ax = plt.subplots(figsize=(10,5))

def update(frame):
    line = ser.readline().decode('utf-8').strip()
    if line:
        voltage = float(line)
        timestamps.append(datetime.now().strftime('%H:%M:%S'))
        voltages.append(voltage)

        ax.clear()
        ax.clear()
        ax.plot(voltages, marker='o', color='blue', label='Voltage')
        ax.axhline(y=threshold, color='red', linestyle='--', label='Threshold')
        ax.set_title('Live Voltage Readings from ESP32')
        ax.set_xlabel('Reading Number')
        ax.set_ylabel('Voltage (V)')
        ax.legend()
        ax.grid(True)

ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()