# -*- coding: utf-8 -*-

import logging
import sys
import pathlib

import serial
from matplotlib import style

style.use('seaborn')

logging.basicConfig(filename=str(pathlib.Path().absolute()) + "\\log\\log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

_PORT = "COM3"
_BAUDRATE = 9600

print("Accessing the data from the all sensors via Arduino")


def connect_to_serial_monitor(port, baudrate):
    print(f'Connecting to Serial w/ port: {port} and baudrate: {baudrate}.')
    return serial.Serial(port, baudrate)


def log_serial_line(ser):
    """
    reads the output of serial from arduino, with could be 3 possibilities
    Soil: X (Soil Moisture reading)
    Temp: X (Air Temperature reading)
    Hum: X (Air Humidity reading)
    """

    read = ser.readline().decode("utf-8")
    print(read)
    sys.stdout.flush()
    sensor = read.split(": ")[0]
    value = read.split(": ")[1].rstrip()

    logging.info([sensor, value])


def serial_to_logfile():
    ser = connect_to_serial_monitor(_PORT, _BAUDRATE)
    while True:
        try:
            log_serial_line(ser)
        except KeyboardInterrupt:
            print("Exiting")
            sys.exit()
