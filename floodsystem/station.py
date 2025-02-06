# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Returns True if the station has a valid typical range, otherwise False"""
        if self.typical_range is None:
            return False  # No data available
        low, high = self.typical_range
        return low < high  # Valid if low < high
    
    def relative_water_level(self): 
        if self.latest_level != None and self.typical_range != None:
            return (self.latest_level-self.typical_range[0])/(self.typical_range[1] - self.typical_range[0])
        return False # no data available
        
def inconsistent_typical_range_stations(stations):
    """Returns a list of stations with inconsistent typical range data."""
    return [station for station in stations if not station.typical_range_consistent()]
