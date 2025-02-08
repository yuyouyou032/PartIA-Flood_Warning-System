
# for station in sh_lst:
#     dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
#     poly, d0 = polyfit(dates, levels, 1)
#     if poly[1] >= 0:
#         severe_lst.append(station)
#     else:
#         high_lst.append(station)
# print("----------severe------------")
# for i in severe_lst:
#     print(i[0].name, i[1])
# print("-----------high---------------")
# for i in high_lst:
#     print(i[0].name, i[1])




# # MEDIUM AND LOW
# lst = stations_level_over_threshold(stations, 0.8)
# ml_lst = [i for i in lst if i not in sh_lst]
# # for i in ml_lst:
# #     print(i[0].name, i[1])

# for station in ml_lst:
#     dates, levels = fetch_measure_levels(station[0].measure_id, dt=timedelta(days=dt))
#     try:
#         poly, d0 = polyfit(dates, levels, 1)
#         print(station[0].name, station[1], poly)
#         if poly[1] >= 0:
#             medium_lst.append(station)
#         else:
#             low_lst.append(station)
#     except:
#         pass
# print("--------------medium---------------")
# for i in medium_lst:
#     print(i[0].name, i[1])
# print("--------------low------------------")
# for i in low_lst:
#     print(i[0].name, i[1])
