import pandas as pd
from utils import show_dataframe_hist
from utils import show_heatmap

if __name__ == "__main__":

    file_name = "../data_frame_edited.csv"

    data_frame = pd.read_csv(file_name)
    print(data_frame.columns)

    histogram_columns = [
        'budget',
        'rating',
        'reviewNumber',
        'potentialAction.priceSpecification.price'
    ]

    data_frame_histogram = data_frame[histogram_columns]



    print(data_frame_histogram.head())
    print(data_frame_histogram.count(0))

    budget_counts = data_frame_histogram[['budget']].groupby(by='budget').agg('count')
    print(budget_counts)
    #print()



    #show_dataframe_hist(data_frame_histogram)
    #show_heatmap(data_frame_histogram)


