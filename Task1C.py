from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

# Define Cambridge city centre coordinates
cambridge_coord = (52.2053, 0.1218)

# Fetch list of stations
stations = build_station_list(use_cache=False)  # Force fresh data fetch

# Get stations within 10 km radius
stations_within_10 = stations_within_radius(stations, cambridge_coord, 10)

# Extract station names and sort them alphabetically
station_names = sorted([station.name for station in stations_within_10])

# Print result
print(station_names)
