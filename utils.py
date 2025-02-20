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

    df = df.drop_duplicates()

    return df

