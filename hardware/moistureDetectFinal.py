#!/usr/bin/env python

import qwiic_soil_moisture_sensor
import time
import sys

def runExample():
    print("\nSparkFun Qwiic Soil Moisture Sensor Example 1\n")
    mySoilSensor = qwiic_soil_moisture_sensor.QwiicSoilMoistureSensor()

    if mySoilSensor.is_connected() == False:
        error_message = "The Qwiic Soil Moisture Sensor device isn't connected to the system. Please check your connection"
        sys.stderr.write(error_message + "\n")
        return

    mySoilSensor.begin()

    print("Initialized.")

    while True:
        mySoilSensor.read_moisture_level()
        print(mySoilSensor.level)
        mySoilSensor.led_on()
        time.sleep(1)
        mySoilSensor.led_off()
        time.sleep(1)

if __name__ == '__main__':
    try:
        runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)

