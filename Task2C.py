# from .utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


# stations for func testing
stations = build_station_list()
update_water_levels(stations)
inconsistent_stations = inconsistent_typical_range_stations(stations)
stations = [i for i in stations if i not in inconsistent_stations]

highest_rel_level_stations = stations_highest_rel_level(stations, 10)
for i in highest_rel_level_stations:
    print(i[0].name, i[1])