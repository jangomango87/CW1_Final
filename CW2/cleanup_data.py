import pandas as pd
import ast


def get_value_from_list_of_dicts(
    list_of_dicts=None,
    key_to_extract=None
):

    set_ids = set()
    for dictionary in list_of_dicts:
        set_ids.add(dictionary[key_to_extract])

    return list(set_ids)



def replace_list_of_dicts_by_value(
    data_frame,
    column_name,
    key_to_extract
):
    for index, row in data_frame.iterrows():
        list_of_dicts = ast.literal_eval(row[column_name])

        id_list = get_value_from_list_of_dicts(
            list_of_dicts=list_of_dicts,
            key_to_extract=key_to_extract
        )

        data_frame.at[index, cusine_col] = id_list

    return data_frame

if __name__ == "__main__":

    file_name = "../CW1/final_data.csv"

    data_frame = pd.read_csv(file_name)

    data_frame_sub = data_frame.iloc[:10]
    # print(data_frame_sub)

    #set_cusine_id = set()

    cusine_col = "characteristics.cuisines"

    #cusines =[]

    key_to_extract = "id"
    #key_to_extract = "url_key"


    data_frame_edited = replace_list_of_dicts_by_value(
        data_frame,
        column_name = cusine_col,
        key_to_extract = key_to_extract
    )

    print(data_frame_edited.head()[cusine_col])

    data_frame_edited.to_csv("../data_frame_edited.csv")



