import numpy as np
from datetime import datetime, timedelta
from matplotlib.dates import date2num, num2date


def polyfit(dates, levels, p):

    dt = date2num(dates)
    if dt.size == 0:
        return np.poly1d([0]), [0]
    p_coeff = np.polyfit(dt-dt[0], levels, p) 
    poly = np.poly1d(p_coeff)

    # print(poly)
    # plt.plot(dt, levels, '.')
    # x1 = np.linspace(dt[0], dt[-1], 30)
    # plt.plot(num2date(x1), poly(x1-dt[0])) # SHIFT
    # plt.xticks(rotation=45);
    # plt.show()

    return poly, dt-dt[0]

# for station in highest_rel_level_stations:
#     dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
#     print(station[0].name, station[1])
#     print(polyfit(dates, levels, 3))




