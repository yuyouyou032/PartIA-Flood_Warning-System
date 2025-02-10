import numpy as np
from datetime import datetime, timedelta
from matplotlib.dates import date2num, num2date


def polyfit(dates, levels, p):
    '''Computes and returns a curve fit of degree p for the dates and water levels input'''
    dt = date2num(dates)
    if dt.size == 0:
        return np.poly1d([0]), [0]
    p_coeff = np.polyfit(dt-dt[0], levels, p) 
    poly = np.poly1d(p_coeff)
    return poly, dt-dt[0]




