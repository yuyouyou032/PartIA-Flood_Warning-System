# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """Returns a list of (station, distance) tuples, where distance is
    the haversine distance from coordinate p. The list is sorted by distance.
    
    Given a list of station objects and a coordinate p
    """
    # Compute distances and store them in a list of tuples
    station_distances = [(station, haversine(station.coord, p)) for station in stations]
    # Sort by distance using utils.sort_by_key
    return sorted_by_key(station_distances, 1)

def stations_within_radius(stations, centre, r):
    """Returns a list of MonitoringStation objects within radius r of a given coordinate.

    Given a list of MonitoringStation objects, a centre, and a radius in kilometers.
    """
    return [station for station in stations if haversine(station.coord, centre) <= r]

def rivers_with_station(stations):
    """Returns a set of river names that have at least one monitoring station.

    Given a list of MonitoringStation objects
    """
    return {station.river for station in stations if station.river}

def stations_by_river(stations):
    """Returns a dictionary mapping river names to a list of station objects.

    Given a list of MonitoringStation objects
    """
    river_dict = {}
    for station in stations:
        if station.river:
            if station.river not in river_dict:
                river_dict[station.river] = []
            river_dict[station.river].append(station)

    return river_dict