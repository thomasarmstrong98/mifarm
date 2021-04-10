import argparse

from src.plot_sensor_values import generate_plot_from_logs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='log filepath for serial output.')
    parser.add_argument('-path', type=str,
                        help='filepath used to read serial output')
    args = parser.parse_args()
    generate_plot_from_logs(args.path)
