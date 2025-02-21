import pandas as pd
import glob
import os

def import_attrition_data():
    path = r'data' # use your path
    all_files = glob.glob(os.path.join(path , '*.csv'))

    print(all_files)

    df_li = []

    for filename in all_files:
        single_df = pd.read_csv(filename, index_col=None, header=0, sep='|')
        df_li.append(single_df)

    df = pd.concat(df_li, axis=0, ignore_index=True)

    # Cleaning

    df = df.drop_duplicates()

    #AT15 & AT16

    df.loc[df["gender"] == "F", "gender"] = "Female"
    df.loc[df["gender"] == "female", "gender"] = "Female"

    df.loc[df["gender"] == "M", "gender"] = "Male"
    df.loc[df["gender"] == "male", "gender"] = "Male"


    df = df.drop("num_kids", axis=1)

    df = df.drop("customer_id", axis=1)

    return df

