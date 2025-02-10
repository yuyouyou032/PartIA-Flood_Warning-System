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
    '''Plots water levels agianst dates for a particular station'''

    # Plot
    plt.plot(dates, levels, label='water lvl')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)


    # annotate typical range low-high
    plt.plot(dates, [station.typical_range[0] for i in range(len(dates))], label='low')
    plt.plot(dates, [station.typical_range[1] for i in range(len(dates))], label='high')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend(loc='upper left')
    plt.show()

# plot_water_levels(station, dates, levels)


def plot_water_level_with_fit(station, dates, levels, p):
    '''Plots water levels agianst dates for a particular station, and add a fit curve with
        the degree of fit specified by p'''

    fig = plt.figure()
    # ax = fig.add_subplot(111)

    poly, d0 = polyfit(dates, levels, p)
    print(poly)
    plt.plot(num2date(d0), levels, '.', label='actual water lvl')
    x1 = np.linspace(d0[0], d0[-1], 90)
    plt.plot(num2date(x1), poly(x1), label='fitted lines')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45);


    # annotate typical range low-high
    plt.plot(num2date(d0), [station.typical_range[0] for i in range(len(d0))], label='low')
    plt.plot(num2date(d0), [station.typical_range[1] for i in range(len(d0))], label='high')

    plt.legend(loc='upper left')
    plt.show()
