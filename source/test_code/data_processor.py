import sys

import pandas as pd


def average(row):
    """Return the average value from the scores."""
    return round((row['Math']+row['English']+row['Science'])/3, 2)


def main(filename):
    dataframe = pd.read_excel(filename,
                              sheet_name=0,
                              header=0,
                              index_col=0,
                              keep_default_na=True
                              )

    dataframe.fillna(0, inplace=True)
    dataframe['average'] = dataframe.apply(lambda row: average(row), axis=1)
    dataframe.to_excel("output.xlsx")


if __name__ == '__main__':
    main(sys.argv[1])
