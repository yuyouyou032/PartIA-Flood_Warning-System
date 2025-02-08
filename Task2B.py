# from floodsystem.utils import sorted_by_key  # noqa
# from haversine import haversine
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations = [i for i in stations if i not in inconsistent_stations]

    over_tol_lst = stations_level_over_threshold(stations, 0.8)

    for i in over_tol_lst:
        print(i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
