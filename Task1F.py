from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""
    # Fetch list of stations
    stations = build_station_list(use_cache=False)  # Force fresh data fetch

    # Find stations with inconsistent typical range data
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Extract station names and sort alphabetically
    station_names = sorted([station.name for station in inconsistent_stations])

    # Print results
    print(station_names)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()