from .utils import sorted_by_key  # noqa
from haversine import haversine
from .station import inconsistent_typical_range_stations, MonitoringStation

from .stationdata import build_station_list, update_water_levels



stations = build_station_list()
update_water_levels(stations)
inconsistent_stations = inconsistent_typical_range_stations(stations)
stations = [i for i in stations if i not in inconsistent_stations]

def stations_level_over_threshold(stations, tol):
    result_lst = []
    for i in stations:
        rel_data = i.relative_water_level()
        if rel_data > tol:
            result_lst.append((i, rel_data))
    return result_lst

# print(stations_level_over_threshold(stations, 0.8))