import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list


# station = build_station_list()[0]
# dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
# print(station, dates, levels)


def plot_water_levels(station, dates, levels):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

# plot_water_levels(station, dates, levels)