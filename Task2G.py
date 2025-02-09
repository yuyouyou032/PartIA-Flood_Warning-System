from datetime import datetime, timedelta
from floodsystem.station import inconsistent_typical_range_stations, MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.utils import sorted_by_key

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
    town_list = {}


    # SEVERE AND HIGH
    sh_lst = stations_level_over_threshold(stations, 1.3)
    lst = stations_level_over_threshold(stations, 1)
    ml_lst = [i for i in lst if i not in sh_lst]
    total = len(sh_lst) + len(ml_lst)
    counter = 0

    for station in sh_lst:
        counter += 1
        print("gathering data, {c} out of {t}".format(c=counter, t=total))
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        poly, d0 = polyfit(dates, levels, 1)
        if station[0].town not in town_list.keys():
                town_list[station[0].town] = [0,0,0,0]
        if poly[1] >= 0:
            severe_lst.append(station)
            town_list[station[0].town][0] += 1
        else:
            high_lst.append(station)
            town_list[station[0].town][1] += 1


    # MEDIUM AND LOW

    for station in ml_lst:
        counter += 1
        print("gathering data, {c} out of {t}".format(c=counter, t=total))
        if station[0].town not in town_list.keys():
            town_list[station[0].town] = [0,0,0,0]
        dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
        try:
            poly, d0 = polyfit(dates, levels, 1)
        except:
            pass
        if poly[1] >= 0:
            medium_lst.append(station)
            town_list[station[0].town][2] += 1
        else:
            low_lst.append(station)
            town_list[station[0].town][3] += 1





    print()
    print("-------------------------------------WARNINGS-------------------------------------")
    risk_scored = []
    for key in town_list.keys():
        risk_scored.append([key, (1*town_list[key][0] + 0.8*town_list[key][1] + 0.5*town_list[key][2] + 0.2*town_list[key][3])])
    risk_scored = sorted_by_key(risk_scored, 1, reverse=True)

    for i in risk_scored:
        print(i[0], "{s} severe risk stations, {h} high risk stations, {m} medium risk stations, {l} low risk stations".format(s=town_list[i[0]][0], h=town_list[i[0]][1], m =town_list[i[0]][2], l = town_list[i[0]][3]))
        if i[1] <0.4:
            print("overall low risk \n")
        elif i[1] <0.8:
            print("overall medium risk \n")
        elif i[1] <1.0:
            print("overall high risk \n")
        else:
            print("overall severe risk \n")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()