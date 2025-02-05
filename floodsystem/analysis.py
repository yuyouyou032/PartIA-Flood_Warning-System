import numpy as np
from datetime import datetime, timedelta
from matplotlib.dates import date2num, num2date


# import matplotlib.pyplot as plt
# from haversine import haversine
# from .station import inconsistent_typical_range_stations, MonitoringStation
# from .stationdata import build_station_list, update_water_levels
# from .flood import stations_highest_rel_level
# from .datafetcher import fetch_measure_levels


# stations = build_station_list()
# update_water_levels(stations)
# inconsistent_stations = inconsistent_typical_range_stations(stations)
# stations = [i for i in stations if i not in inconsistent_stations]
# highest_rel_level_stations = stations_highest_rel_level(stations, 2)
# dt = 2

def polyfit(dates, levels, p):

    dt = date2num(dates)
    p_coeff = np.polyfit(dt-dt[0], levels, p) 
    poly = np.poly1d(p_coeff)

    # print(poly)
    # plt.plot(dt, levels, '.')
    # x1 = np.linspace(dt[0], dt[-1], 30)
    # plt.plot(num2date(x1), poly(x1-dt[0])) # SHIFT
    # plt.xticks(rotation=45);
    # plt.show()

    return poly, dt-dt[0]

# for station in highest_rel_level_stations:
#     dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
#     print(station[0].name, station[1])
#     print(polyfit(dates, levels, 3))




