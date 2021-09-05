import folium
import pandas as pd
import geopy
from sklearn import preprocessing, cluster


def get_city_location_geopy(
    city
):
    # get location
    locator = geopy.geocoders.Nominatim(user_agent="MyCoder")
    location = locator.geocode(city)
    print(location)
    # keep latitude and longitude only
    location = [location.latitude, location.longitude]

    return location


def get_folium_map(
    df=None,
    location=None,
    x='geo.latitude',
    y='geo.longitude',
    color='budget',
    size='reviewNumber',
    popup='rating',
    lst_colors=["red", "orange", "green"]
):
    # create color column
    data = df.copy()
    lst_elements = sorted(list(df[color].unique()))

    data["color"] = data[color].apply(lambda x:
                                      lst_colors[lst_elements.index(x)])

    print(data.head())

    # create size column (scaled)
    scaler = preprocessing.MinMaxScaler(feature_range=(3, 15))
    data["size"] = scaler.fit_transform(
        data[size].values.reshape(-1, 1)).reshape(-1)

    # initialize the map with the starting location
    map_ = folium.Map(
        location=location,
        tiles="cartodbpositron",
        zoom_start=11
    )

    # add points
    data.apply(lambda row: folium.CircleMarker(
               location=[row[x], row[y]], popup=row[popup],
               color=row["color"], fill=True,
               radius=row["size"]).add_to(map_), axis=1)
    # add html legend
    legend_html = """<div style="position:fixed; bottom:10px; left:10px; border:2px solid black; z-index:9999; font-size:14px;">&nbsp;<b>"""+color+""":</b><br>"""
    for i in lst_elements:
        legend_html = legend_html+"""&nbsp;<i class="fa fa-circle
         fa-1x" style="color:"""+lst_colors[lst_elements.index(i)]+"""">
         </i>&nbsp;"""+str(i)+"""<br>"""
    legend_html = legend_html+"""</div>"""

    map_.get_root().html.add_child(folium.Element(legend_html))

    return map_


if __name__ == "__main__":

    data_file = "../CW1/final_data.csv"
    df_final_data = pd.read_csv(data_file)

    #data = df_final_data.copy()

    print(df_final_data.columns)
    city = "Lahore"
    city_df = "lahore"
    df_city_data = df_final_data.loc[df_final_data["city"]==city_df]

    location = get_city_location_geopy(city)

    map_ = get_folium_map(
        df=df_city_data,
        location=location,
        x='geo.latitude',
        y='geo.longitude',
        color='budget',
        size='reviewNumber',
        popup='rating',
        lst_colors=["red", "orange", "green"]
    )

    # plot the map
    map_.save("index.html")
