import pandas as pd
from typing import NoReturn


def formatted_file(input_file: str) -> pd.DataFrame:
    """Форматирование файла
    Возвращает фрейм  данных с добавлением столбцов"""
    df = pd.read_csv(file)

    df["Day"] = pd.to_datetime(df.Day, format="%Y-%m-%d")
    df["Day1"] = df["Day"].dt.date  
    df["Year"] = df["Day"].dt.year
    return df


def write_to_file(input_file: str, year: int) -> NoReturn:
    """input_file - файл с набором данных
    возвращает ничего"""
    df = formatted_file(input_file)

    df = df[df["Year"] == year]
    data = str(df["Day1"].iloc[0]).replace("-", "") + "_" + str(df["Day1"].iloc[df.shape[0] - 1]).replace("-", "")
    del df["Year"]
    del df["Day1"]
    df.to_csv(data + ".csv", index=False)


def range_of_date(input_file: str) -> list :
    """Диапазон значений временных в наборе данных
    input_file - файл с набором данных
    возвращает список с первым и последним годом в наборе данных"""
    df = formatted_file(input_file)

    start_range = df["Year"].iat[0]
    end_range = df["Year"].iat[-1]
    return [start_range, end_range]


if __name__ == "__main__":

    file = "C:/Users/esh20/Desktop/dataset.csv"

    range_of_years = range_of_date(file)
    for years in range(range_of_years[0], range_of_years[1] - 1, -1):
        write_to_file(file, years)

print("Pls, htlp me, pls hel me.. pls... help... this night is very...very hard..")
