import geopandas
import matplotlib.pyplot as plt
import contextily as ctx

def get_sub_path(
    filename = None,
    no_splits = None,
    index = 1
):
    if not no_splits:
        return filename.rsplit("/")[index]

    return filename.rsplit("/", no_splits)[index]

if __name__ == "__main__":

    #shape_file = "../shape_files/Union_Council/Union_Council.shp"
    shape_file = "../shape_files/Admin_Boundaries/National_Consituency/National_Constituency_with_Projected_2010_Population.shp"
    df = geopandas.read_file(shape_file)

    filename = get_sub_path(
        shape_file,
        1,
        -1
    )+".csv"

    data_file = "../CW1/final_data.csv"
    df_data = geopandas.read_file(data_file)
    df_data = df_data.loc[df_data["city"]=="islamabad"]
    geometry = geopandas.points_from_xy(df_data["geo.longitude"], df_data["geo.latitude"])
    gdf_data = geopandas.GeoDataFrame(
        df_data, geometry=geometry)
    #df.to_csv(filename)
    #print(df.columns)
    df_toMap = df.loc[df["District"]=="Islamabad"]
    #df_toMap = df

    print(gdf_data.head())


    ##ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

    ##plt.show()

    #df_toMap = df_toMap.to_crs(epsg=3857)
    ##df_to_plot = df_data.to_crs(epsg=3857)

    ax = df_toMap.plot(figsize=(20, 20), alpha=0.2, edgecolor='k')

    #df_data.plot(figsize=(20, 20), alpha=0.2, edgecolor='k')

    df_data.plot(ax=ax)
    ctx.add_basemap(ax)

    plt.show()


