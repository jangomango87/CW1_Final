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
    data_frame=None,
    column_name=None,
    key_to_extract = "id"
):
    for index, row in data_frame.iterrows():
        list_of_dicts = ast.literal_eval(row[column_name])

        id_list = get_value_from_list_of_dicts(
            list_of_dicts=list_of_dicts,
            key_to_extract=key_to_extract
        )

        data_frame.at[index, column_name] = id_list

    return data_frame

if __name__ == "__main__":

    file_name = "../CW1/final_data.csv"

    data_frame = pd.read_csv(file_name)

    data_frame_sub = data_frame
    # print(data_frame_sub)

    #set_cusine_id = set()

    target_col = {
        "characteristics.cuisines": "id",
        "characteristics.food_characteristics": "name"
    }

    #cusines =[]

    #key_to_extract = "url_key"


    for key, value in target_col.items():
        data_frame_edited = replace_list_of_dicts_by_value(
            data_frame,
            column_name = key,
            key_to_extract = value
        )


    print(data_frame_edited.head())

#    data_frame_edited.to_csv("../data_frame_edited.csv")



