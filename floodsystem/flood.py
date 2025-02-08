from .utils import sorted_by_key  # noqa
# from haversine import haversine
from .station import inconsistent_typical_range_stations, MonitoringStation
from .stationdata import build_station_list, update_water_levels


# stations for func testing
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
    sorted_result_lst = sorted_by_key(result_lst, 1, reverse=True)
    return sorted_result_lst

# print(stations_level_over_threshold(stations, 0.8))

def stations_highest_rel_level(stations, N):
    over_thresh_stations = stations_level_over_threshold(stations, 0)
    ranked_over_thresh_stations = sorted_by_key(over_thresh_stations, 1, reverse=True)
    return ranked_over_thresh_stations[:N]


