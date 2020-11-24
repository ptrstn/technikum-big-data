import pandas


def spread_unihan(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    dataframe = dataframe.pivot(index="unicode", columns="field", values="description")
    dataframe.reset_index(inplace=True)
    return dataframe
