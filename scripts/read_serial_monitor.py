import argparse
from src.serial_monitor import serial_to_logfile

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Port to read serial monitor from.')
    parser.add_argument('-port', type=str,
                        help='Serial port.')
    args = parser.parse_args()
    serial_to_logfile(args.port)
