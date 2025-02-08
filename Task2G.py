from datetime import datetime, timedelta
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit

# severe: high above average high (1.3+) and positive gradient
# high: high above average high (1.3+), gradient not as positive
# moderate: >0.8, <1.3, positive gradient
# low: >0.8, <1.3, gradient not as positive
def run():

    stations = build_station_list()
    update_water_levels(stations)
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    stations = [i for i in stations if i not in inconsistent_stations]

    dt = 2
    severe_lst = []
    high_lst = []
    medium_lst = []
    low_lst = []
    error_lst = []


    # SEVERE AND HIGH
    sh_lst = stations_level_over_threshold(stations, 1.3)
    for i in sh_lst:
        print(i[0].name, i[1])
    print("------------- warnings --------------")
    for station in sh_lst:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, 1)
        if poly[1] >= 0:
            severe_lst.append(station)
        else:
            high_lst.append(station)
    print("----------severe risk------------")
    for i in severe_lst:
        print(i[0].name, i[1])
    print("-----------high risk---------------")
    for i in high_lst:
        print(i[0].name, i[1])




    # MEDIUM AND LOW
    lst = stations_level_over_threshold(stations, 0.8)
    ml_lst = [i for i in lst if i not in sh_lst]

    for station in ml_lst:
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        try:
            poly, d0 = polyfit(dates, levels, 1)
            if poly[1] >= 0:
                medium_lst.append(station)
            else:
                low_lst.append(station)
        except:
            pass
    print("--------------medium risk---------------")
    for i in medium_lst:
        print(i[0].name, i[1])
    print("--------------low risk------------------")
    for i in low_lst:
        print(i[0].name, i[1])

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()