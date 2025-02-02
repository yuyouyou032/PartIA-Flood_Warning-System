from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

# Fetch list of stations
stations = build_station_list(use_cache=False)  # Force fresh fetch

# Get unique rivers with monitoring stations
rivers = rivers_with_station(stations)

# Print total number of rivers and first 10 in alphabetical order
print(f"{len(rivers)} rivers have at least one monitoring station.")
print(f"First 10: {sorted(rivers)[:10]}")

# Get stations by river
stations_by_river_dict = stations_by_river(stations)

# Print stations on specific rivers
for river_name in ["River Aire", "River Cam", "River Thames"]:
    station_names = sorted([s.name for s in stations_by_river_dict[river_name]])
    print(f"\nStations on {river_name}:")
    print(station_names) 

