import serial
import time
import csv

# --- SETTINGS ---
PORT = '/dev/ttyACM0'
BAUD = 115200
FILE = 'microbit_data.csv'

# Connect to micro:bit
try:
    ser = serial.Serial(PORT, BAUD)
    print("Connected!")
except:
    print("Could not connect. Check port.")
    exit()

# Ask user for info
label = input("Enter label (example: cafeteria, outside, closet): ")
duration = int(input("How many seconds to record? "))

# Open CSV file to output serial data to
file = open(FILE, 'w', newline='')
writer = csv.writer(file)

# Write header of CSV (replace with your feature names)
writer.writerow(['Temp', 'Light', 'Sound', 'Label'])

print("\nRecording...\n")

start = time.time()

# Main loop to read serial data at a regular interval and write to CSV
while time.time() - start < duration:
    if ser.in_waiting:
        line = ser.readline().decode().strip()
        parts = line.split(',')

        if len(parts) >= 3:
            try:
                # modify this based on which features you are using 
                temp = float(parts[0])
                light = int(parts[1])
                sound = int(parts[2])

                writer.writerow([temp, light, sound, label])
                print(temp, light, sound)

            except:
                pass  # ignore malformed data

print("\nDone reading data. Saved to " + FILE + ". Make sure to copy this over to another file so it doesn't get overwritten next time you record data.")

file.close()
ser.close()