# -*- coding: utf-8 -*-

import datetime as dt
import logging
import pathlib
import sys

import serial
from matplotlib import style
from src.utils.directory_navigation import get_path_to_rel_location

style.use('seaborn')

logging.basicConfig(
    filename=str(get_path_to_rel_location("mifarm") / "log" / f"{dt.datetime.today().strftime('%Y-%m-%d')}.txt"),
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


def catch_unwanted_serial_lines(line):
    unwanted_lines = ["Adafruit AM2320 Basic Test\r\n", 0]
    if line in unwanted_lines:
        return None
    else:
        return line


def log_serial_line(ser):
    """
    reads the output of serial from arduino, with could be 3 possibilities
    Soil: X (Soil Moisture reading)
    Temp: X (Air Temperature reading)
    Hum: X (Air Humidity reading)
    """

    read = ser.readline().decode("utf-8")
    if catch_unwanted_serial_lines(read) is None:
        sys.stdout.flush()
    else:
        sys.stdout.flush()
        sensor = read.split(": ")[0]
        value = read.split(": ")[1].rstrip()

        logging.info([sensor, value])


def serial_to_logfile(port):
    ser = connect_to_serial_monitor(port, _BAUDRATE)
    while True:
        try:
            log_serial_line(ser)
        except KeyboardInterrupt:
            print("Exiting")
            sys.exit()
