from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1E"""
    # Fetch list of stations
    stations = build_station_list(use_cache=False)  # Force fresh fetch

    # Get top 9 rivers by station count
    top_rivers = rivers_by_station_number(stations, 9)

    # Print results
    print(top_rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()