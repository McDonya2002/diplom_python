import numpy as np
import ApiController


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def jarvis_convex_hull(points):
    n = len(points)
    if n < 3:
        return []
    hull = []
    leftmost = min(points)
    p = leftmost
    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if r == p:
                continue
            if orientation(p, q, r) == 2:
                q = r
        p = q
        if p == leftmost:
            break
    return hull


unique_clusters = ApiController.GET_unique_cluster_numbers()
print(unique_clusters)


def find_by_lat_and_long(lat, long, data_array):
    for i in range(len(data_array)):
        if lat == data_array[i][0] and long == data_array[i][1]:
            return (int(data_array[i][3]))


for i in range(unique_clusters):
    points = ApiController.GET_points_by_cluster(i)
    data_array = np.array([[point['longitude'], point['latitude'], point['cluster'], point['id']] for point in points])
    coordinates = data_array[:, :2]
    points_tuples = [(x, y) for x, y in coordinates]
    convex_hull_points = jarvis_convex_hull(points_tuples)
    for j in range(len(convex_hull_points)):
        ApiController.PATCH_points_place(
            find_by_lat_and_long(convex_hull_points[j][0], convex_hull_points[j][1], data_array), j)



