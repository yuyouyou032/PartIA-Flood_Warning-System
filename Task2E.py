# from .utils import sorted_by_key  # noqa
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta



def run():
    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations = [i for i in stations if i not in inconsistent_stations]


    highest_rel_level_stations = stations_highest_rel_level(stations, 5)
    dt = 10
    for i in highest_rel_level_stations:
        print(i[0].name, i[1])


    for station in highest_rel_level_stations:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        # print(levels)
        plot_water_levels(station[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()