# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    # Test typical_range_consistent method
    assert s.typical_range_consistent() == True  # Expected True because low < high in the range
    
    # Test with invalid range (low > high)
    invalid_trange = (4.0, 3.0)  # Invalid range (low > high)
    s_invalid = MonitoringStation(s_id, m_id, label, coord, invalid_trange, river, town)
    assert s_invalid.typical_range_consistent() == False  # Expected False because low > high
    
    # Test with None as typical_range
    s_none = MonitoringStation(s_id, m_id, label, coord, None, river, town)
    assert s_none.typical_range_consistent() == False  # Expected False because range is None

def test_inconsistent_typical_range_stations():
    # Create a list of MonitoringStation instances with various typical_range values
    
    # Valid station (low < high)
    s1 = MonitoringStation("s1", "m1", "Station 1", (-2.0, 4.0), (-2.3, 3.4445), "River A", "Town A")
    
    # Invalid station (low > high)
    s2 = MonitoringStation("s2", "m2", "Station 2", (-2.0, 4.0), (4.0, 3.0), "River B", "Town B")
    
    # Station with None as typical_range
    s3 = MonitoringStation("s3", "m3", "Station 3", (-2.0, 4.0), None, "River C", "Town C")
    
    # Another valid station (low < high)
    s4 = MonitoringStation("s4", "m4", "Station 4", (-2.0, 4.0), (1.0, 2.0), "River D", "Town D")

    # List of stations
    stations = [s1, s2, s3, s4]

    # Call inconsistent_typical_range_stations to get stations with inconsistent typical ranges
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Assert that the correct stations are returned
    assert len(inconsistent_stations) == 2  # We expect two stations to have inconsistent ranges
    assert s2 in inconsistent_stations  # s2 has an invalid range (low > high)
    assert s3 in inconsistent_stations  # s3 has None as the typical_range

    # Assert that the valid stations are not in the result
    assert s1 not in inconsistent_stations  # s1 has a valid range
    assert s4 not in inconsistent_stations  # s4 has a valid range


