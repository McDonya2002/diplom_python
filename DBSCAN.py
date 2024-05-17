import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import ApiController


def plot_clusters(points, labels):
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = points[class_member_mask]
        plt.plot(xy[:, 1], xy[:, 0], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.title('Clusters')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()


def dbscan_clustering(points, eps=0.011, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(points)
    data_with_labels = np.column_stack((points, labels))
    return data_with_labels


data = ApiController.GET_all_points()
data_array = np.array([[point['latitude'], point['longitude']] for point in data])
data_with_labels = dbscan_clustering(data_array)

id_and_labels = np.column_stack((np.array([point['id'] for point in data]), data_with_labels[:, -1])).astype(int)

for i in range(len(id_and_labels)):
    ApiController.PATCH_points_clusters(id_and_labels[i][0], id_and_labels[i][1])

plot_clusters(data_array, data_with_labels[:, -1])



