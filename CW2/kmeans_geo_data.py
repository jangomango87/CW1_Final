from sklearn import cluster

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.cluster.vq import vq

from geo_folium_experiment import get_folium_map
from geo_folium_experiment import get_city_location_geopy


def get_optimal_cluster(
    df,
    variable,
    max_k=10
):
    data= df.copy()
    X = data[variable]
    # iterations
    different_k_clusters = []

    for no_clusters in range(1, max_k+1):
        # Check if number of rows is greater than required max clusters
        if len(X) >= no_clusters:
            model = cluster.KMeans(
                n_clusters=no_clusters,
                init='k-means++',
                max_iter=300,
                n_init=10,
                random_state=0
            )
            model.fit(X)
            different_k_clusters.append(model.inertia_)
    # best k: the lowest derivative

    k = [i*100 for i in np.diff(different_k_clusters, 2)].index(
        min(
            [i*100 for i in np.diff(different_k_clusters, 2)]
        )
    )

    return k, different_k_clusters


def get_clustering_model(
    k=6,
    init='k-means++'
):

    model = cluster.KMeans(n_clusters=k, init='k-means++')
    return model


def data_frame_with_cluster_data(
    df,
    variable,
    model
):

    X = df[variables]
    # clustering
    dtf_X = X.copy()
    dtf_X["cluster"] = model.fit_predict(X)

    return dtf_X, model

# find real centroids


def get_cluster_centroid(
    model=None,
    dtf_X=None,
):
    closest, distances = vq(
        model.cluster_centers_,
        dtf_X.drop("cluster", axis=1).values
    )
    dtf_X["centroids"] = 0

    for i in closest:
        dtf_X["centroids"].iloc[i] = 1

    return dtf_X


if __name__ == "__main__":

    data_file = "../CW1/final_data.csv"
    df_final_data = pd.read_csv(data_file)
    city = "islamabad"
    df_city_data = df_final_data.loc[df_final_data["city"] == city]

    variables = [
        'geo.latitude',
        'geo.longitude'
    ]

    k, inertia = get_optimal_cluster(
        df_city_data,
        variable=variables,
        max_k=10
    )

    plt.plot(inertia)
    plt.show()

    model = get_clustering_model(
        k=k,
        init='k-means++'
    )
    data_frame_cluster, model = data_frame_with_cluster_data(
        df=df_city_data,
        variable=variables,
        model=model
    )
    data_frame_cluster = get_cluster_centroid(
        model=model,
        dtf_X=data_frame_cluster
    )

    # add clustering info to the original dataset
    df_city_data[["cluster", "centroids"]] = data_frame_cluster[["cluster", "centroids"]]

    print(df_city_data.head())

    location = get_city_location_geopy("Islamabad")

    map_ = get_folium_map(
        df=data_frame_cluster,
        location=location,
        x='geo.latitude',
        y='geo.longitude',
        color='cluster',
        size='cluster',
        popup='centroids',
        lst_colors=["red", "orange", "green", "purple", "blue", "yellow"]
    )

    map_.save("cluster.html")
