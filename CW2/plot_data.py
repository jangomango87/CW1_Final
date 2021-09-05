import pandas as pd
from utils import show_dataframe_hist
from utils import show_heatmap

if __name__ == "__main__":

    file_name = "../data_frame_edited.csv"

    data_frame = pd.read_csv(file_name)

    #print(data_frame.head())

    #show_dataframe_hist(data_frame)
    show_heatmap(data_frame)


