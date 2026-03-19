# Micro:bit KNN Demo

This project is a small machine-learning demo for the BBC micro:bit using the **K-Nearest Neighbors (KNN)** algorithm.  
It shows how a device can classify environments based on simple sensor readings.

## Purpose

This project demonstrates the basic ML workflow on embedded devices with limited hardware capabilities.

1. **Collect labeled examples** from micro:bit sensors (e.g. temperature, light intensity and the corresponding environment of measurement).
2. **Store those examples** as training data. 
3. **Classify new sensor readings** by comparing them to the training set with KNN.
4. **Predict the class** for an unknown data point, simply by measuring data from the sensors.

## Project structure 

- [`microbit_firmware.py`](./microbit_firmware.py): contains the code to be run on the micro:bit. Prints out sensor data at a regular interval
- [`serial_reader.py`](./serial_reader.py): reads the Serial port for the data coming from the micro:bit and saves it to [`microbit_data.csv`](./microbit_data.csv)
  - this data can be manually cleaned, tagged, and copied to [`compile_data.csv`](./compile_data.csv)
- [`knntrainer.py`](./knntrainer.py): reads training data from [`compile_data.csv`](./compile_data.csv) and fits a KNN Classifier. Allows user to enter new data points for it to predict the class.

## Running the demo

1. Flash [`microbit_firmware.py`](./microbit_firmware.py) to the micro:bit. One way to accomplish this is using the [uflash](https://uflash.readthedocs.io/en/latest/) utility, or with the Mu code editor.
2. Place the micro:bit in the first environment and run [`serial_reader.py`](./serial_reader.py). Once enough data is collected, copy it to the compiled data csv. Repeat this step two more times for distinct environments.
3. Run [`knntrainer.py`](./knntrainer.py). Enter a sample data point (this can be collected from the micro:bit or made up within a reasonable margin). The script should predict which environment was most resembled by the test data point.
