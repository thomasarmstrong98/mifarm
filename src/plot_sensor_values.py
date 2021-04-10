import datetime as dt

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

VALID_SENSORS = ["Soil", "Temp", "Hum"]


def animate(i, logfile, sensor_axes, sensor_axes_config):
    graph_data = open(logfile, 'r').read()
    lines = graph_data.split('\n')
    data = dict()

    if len(lines) <= 1:
        print("No data being collected")
        raise RuntimeError

    for line in lines:
        if len(line) > 1:
            t, obs = line.split(" root INFO ")
            t = dt.datetime.strptime(t, "%H:%M:%S,%f")
            sensor = obs.split(",")[0][1:]
            sensor = sensor.replace("'", "")
            sensor_obs = float(obs.split(",")[1][:-1].replace("'", ""))

            if sensor not in data:
                data[sensor] = dict()
                data[sensor][t] = {sensor: sensor_obs}
            else:
                data[sensor][t] = {sensor: sensor_obs}

    for sensor in data.keys():
        if sensor not in VALID_SENSORS:
            print(f"Found unkown sensor observation {sensor}")
        else:
            tmp_df = pd.DataFrame.from_dict(data[sensor], orient="index")
            sensor_axes[sensor].clear()
            sensor_axes[sensor].plot(tmp_df.rolling(20).mean(), color=sensor_axes_config[sensor]["color"], label=sensor)
            sensor_axes[sensor].figure.set_size_inches(7, 5)
            sensor_axes[sensor].legend(loc="upper right")


def generate_plot_from_logs(logfile):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    fig.tight_layout()

    sensor_axes = {
        "Temp": ax1,
        "Hum": ax2,
        "Soil": ax3
    }

    sensor_axes_config = {
        "Soil": {"color": "teal"},
        "Hum": {"color": "green"},
        "Temp": {"color": "red"},
    }

    ani = animation.FuncAnimation(fig, animate, fargs=(logfile, sensor_axes, sensor_axes_config,), interval=1000)
    plt.show()
