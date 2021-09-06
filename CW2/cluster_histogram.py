import pandas as pd

from utils import show_dataframe_hist

def get_cluster_data_frame(
    data_frame = None,
    cluster_no = None
):
    data = data_frame.loc[data_frame["cluster"] == cluster_no]
    return  data



if __name__ == "__main__":
    file_name = "./cluster_data.csv"

    data_frame = pd.read_csv(file_name)


    cluster_data = get_cluster_data_frame(
        data_frame = data_frame,
        cluster_no= 0
    )

    show_dataframe_hist(cluster_data)


    


