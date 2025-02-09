from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from datetime import datetime, timedelta


stations = build_station_list()
update_water_levels(stations)
inconsistent_stations = inconsistent_typical_range_stations(stations)
stations = [i for i in stations if i not in inconsistent_stations]
station = stations[0]

def test_plot_water_levels():
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    plot_water_levels(station, dates, levels)
        
def test_plot_water_level_with_fit():
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=dt))
    plot_water_level_with_fit(station, dates, levels, 2)