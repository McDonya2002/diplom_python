import requests

url_get_point = "https://localhost:8443/api/v1/admin/points"
url_get_all_points = "https://localhost:8443/api/v1/admin/points"
url_get_all_points_with_cluster = "https://localhost:8443/api/v1/admin/points/clusters"
url_patch_points_clusters = "https://localhost:8443/api/v1/admin/points/clusters"
url_patch_points_order = "https://localhost:8443/api/v1/admin/points/place"
url_post_points = "https://localhost:8443/api/v1/admin/points"
url_get_max_id = "https://localhost:8443/api/v1/admin/points/max_id"
url_get_min_id = "https://localhost:8443/api/v1/admin/points/min_id"
url_get_unique_cluster_numbers = "https://localhost:8443/api/v1/admin/cluster"


def GET_all_points():
    response = requests.get(url_get_all_points)
    if response.status_code == 200:
        data = response.json()
        return data


def GET_points_with_cluster():
    response = requests.get(url_get_all_points_with_cluster)
    if response.status_code == 200:
        data = response.json()


def PATCH_points_clusters(id, cluster_number):
    url = url_patch_points_clusters + "/" + str(id) + "/" + str(cluster_number)
    response = requests.patch(url)
    if response.status_code == 200:
        print(response.status_code)
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def POST_point(point):
    data = point
    response = requests.post(url_post_points, json=data,
                             headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        print("Список точек успешно отправлен")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def PATCH_points_place(id, place):
    url = url_patch_points_order + "/" + str(id) + "/" + str(place)
    response = requests.patch(url)
    if response.status_code == 200:
        print(response.status_code)
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def GET_max_id():
    response = requests.get(url_get_max_id)
    if response.status_code == 200:
        return response.json()


def GET_min_id():
    response = requests.get(url_get_min_id)
    if response.status_code == 200:
        print(response.json())
        return response.json()


def GET_point_by_id(id):
    print(url_get_all_points + "/" + id)
    response = requests.get(url_get_all_points + "/" + id)

    print(response.json())
    return response.json()


def GET_unique_cluster_numbers():
    print(url_get_unique_cluster_numbers)
    response = requests.get(url_get_unique_cluster_numbers)
    return response.json()


def GET_points_by_cluster(cluster):
    url = "https://localhost:8443/api/v1/admin/points/cluster/" + str(cluster)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data



