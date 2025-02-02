from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

# Fetch list of stations
stations = build_station_list(use_cache=False)  # Force fresh data fetch

# Find stations with inconsistent typical range data
inconsistent_stations = inconsistent_typical_range_stations(stations)

# Extract station names and sort alphabetically
station_names = sorted([station.name for station in inconsistent_stations])

# Print results
print(station_names)
