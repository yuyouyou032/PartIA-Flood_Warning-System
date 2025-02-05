import numpy as np
from datetime import datetime, timedelta
from matplotlib.dates import date2num, num2date
import matplotlib.pyplot as plt



from haversine import haversine
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit


stations = build_station_list()
update_water_levels(stations)
inconsistent_stations = inconsistent_typical_range_stations(stations)
stations = [i for i in stations if i not in inconsistent_stations]
highest_rel_level_stations = stations_highest_rel_level(stations, 5)
dt = 2

for station in highest_rel_level_stations:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
    plot_water_level_with_fit(station, dates, levels, 4)