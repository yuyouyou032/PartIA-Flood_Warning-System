import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list
from .analysis import polyfit
import numpy as np
from matplotlib.dates import date2num, num2date

from .flood import stations_highest_rel_level



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


def plot_water_level_with_fit(station, dates, levels, p):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    poly, d0 = polyfit(dates, levels, p)
    print(poly)
    plt.plot(num2date(d0), levels, '.')
    x1 = np.linspace(d0[0], d0[-1], 90)
    plt.plot(num2date(x1), poly(x1))
    plt.title(station[0].name)
    plt.xticks(rotation=45);


    # annotate typical range low-high
    plt.plot(num2date(d0), [station[0].typical_range[0] for i in range(len(d0))])
    plt.plot(num2date(d0), [station[0].typical_range[1] for i in range(len(d0))])

    plt.show()
