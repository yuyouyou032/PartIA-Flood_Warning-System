from floodsystem.utils import sorted_by_key  # noqa
# from haversine import haversine
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


stations = build_station_list()
update_water_levels(stations)
inconsistent_stations = inconsistent_typical_range_stations(stations)
stations = [i for i in stations if i not in inconsistent_stations]


def test_stations_level_over_threshold():
    over_thresh_lst = stations_level_over_threshold(stations, 0.5)
    assert len(over_thresh_lst) > 0

def test_stations_highest_rel_level():
    ranked_lst = stations_highest_rel_level(stations, 10)
    assert len(ranked_lst) == 10