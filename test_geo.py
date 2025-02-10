"""Unit test for the geo module"""
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from haversine import haversine
from floodsystem.geo import *
# def mock_stations():
#     return [
#         MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
#         MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
#         MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
#         MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),
#     ]

mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]



def test_stations_by_distance():
    mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]
    p = (52.206, 0.122)  # Reference point
    result = stations_by_distance(mock_stations, p)
    assert result == sorted(result, key=lambda x: x[1])
    for station, distance in result:
        assert isinstance(station, MonitoringStation)
        assert isinstance(distance, float)
        assert distance >= 0

def test_stations_within_radius():
    mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]

    centre = (52.205, 0.1218)
    r = 10  # Radius in km
    result = stations_within_radius(mock_stations, centre, r)
    assert isinstance(result, list)
    for station in result:
        assert isinstance(station, MonitoringStation)
        assert haversine(station.coord, centre) <= r

def test_rivers_with_station():
    mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]

    result = rivers_with_station(mock_stations)
    assert isinstance(result, set)
    assert result == {"River A", "River B", "River C"}

def test_stations_by_river():
    mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]

    result = stations_by_river(mock_stations)
    
    assert isinstance(result, dict)
    assert set(result.keys()) == {"River A", "River B", "River C"}
    assert len(result["River A"]) == 2
    assert len(result["River B"]) == 1
    assert len(result["River C"]) == 1

def test_rivers_by_station_number():

    mock_stations = [        MonitoringStation("s1", "m1", "Station 1", (52.205, 0.1218), None, "River A", "Town A"),
    MonitoringStation("s2", "m2", "Station 2", (52.2053, 0.1219), None, "River A", "Town B"),
    MonitoringStation("s3", "m3", "Station 3", (52.206, 0.122), None, "River B", "Town C"),
    MonitoringStation("s4", "m4", "Station 4", (52.207, 0.123), None, "River C", "Town D"),]

    result = rivers_by_station_number(mock_stations, 2)
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result)
    assert len(result) >= 2  # At least N rivers should be returned

