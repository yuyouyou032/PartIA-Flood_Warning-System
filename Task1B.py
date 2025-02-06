from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""
    # Define Cambridge city centre coordinates
    cambridge_coord = (52.2053, 0.1218)

    # Fetch list of stations objects
    stations = build_station_list(use_cache=False)  # Force fresh data fetch

    # Get stations sorted by distance
    sorted_stations = stations_by_distance(stations, cambridge_coord)
    
    # Extract a list of tuples (station name, town, distance) for the top 10 closest and the top 10 furthest stations from the Cambridge city centre
    closest_10 = [(s.name, s.town, d) for s, d in sorted_stations[:10]]
    furthest_10 = [(s.name, s.town, d) for s, d in sorted_stations[-10:]]

    # Print results
    print(closest_10)
    print(furthest_10)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
