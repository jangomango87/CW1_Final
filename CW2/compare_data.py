import pandas as pd
import ast
import json
# def compare_dataframes_by_column(
#    df1,
#    df2,
#    comparison_column
# ):
#    return
#
# def get_data_frame_comparison(
#    df1,
#    df2,
#    comparison_column
# ):
#    result = {
#        "no_of_duplicate_records_by_code": None,
#        "index_of_new_record":
#    }
#
#    return


# How many new restaurant codes?

# How many known restaurants have changed values?

# Has Restaurant moved? (geo coordinate comparison)

# Has Budget Changed?

# Has Cusine changed

# Create


if __name__ == "__main__":

    file_name = "../CW1/final_data.csv"

    data_frame = pd.read_csv(file_name)

    data_frame_sub = data_frame.iloc[:10]
    #print(data_frame_sub)

    set_cusine_id = set()

    cusine_col = "characteristics.cuisines"

    cusines =[] 

    for index, row in data_frame.iterrows():
        characteristics_cusine = ast.literal_eval(row[cusine_col])
        for dictionary in characteristics_cusine:
            if dictionary["id"] not in set_cusine_id:
                cusines.append(dictionary)
                set_cusine_id.add(dictionary["id"])



            
    cusine_dataframe = pd.DataFrame(cusines)


    print(cusine_dataframe)





