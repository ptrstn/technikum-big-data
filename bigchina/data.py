import pathlib
from zipfile import ZipFile

import pandas
import requests

UNIHAN_ZIP_URL = "https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip"
UNIHAN_BASE_PATH = pathlib.Path("data", "unihan")
UNIHAN_FILE_PATTERN = "Unihan_*.txt"

HSK_BASE_PATH = pathlib.Path("data", "hsk")
HSK_FILE_PATTERN = "hsk*.txt"


def download_file(url, download_to_path, quiet=False):
    if not quiet:
        print(f"Downloading {url} to {download_to_path}...")
    response = requests.get(url, allow_redirects=True)
    download_to_path = pathlib.Path(download_to_path)
    download_to_path.parent.mkdir(parents=True, exist_ok=True)
    with open(download_to_path, "wb") as file:
        file.write(response.content)


def extract_zip(zip_file_path, extract_to_path, quiet=False):
    if not quiet:
        print(f"Extracting {zip_file_path} to {extract_to_path}...")
    with ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall(extract_to_path)


# ------------------------
# Unihan
# ------------------------


def download_unihan_zip(
        base_path=UNIHAN_BASE_PATH, url=UNIHAN_ZIP_URL, force=False, quiet=False
):
    file_name = pathlib.Path(url).name
    file_path = pathlib.Path(base_path, file_name)
    if not file_path.exists() or force:
        download_file(url, file_path, quiet=quiet)
        extract_zip(file_path, base_path, quiet=quiet)


def read_unihan_file(path):
    column_names = ["unicode", "field", "description"]
    return pandas.read_csv(path, sep="\t", names=column_names, comment="#")


def list_unihan_file_paths(base_path=UNIHAN_BASE_PATH):
    return list(pathlib.Path(base_path).glob(UNIHAN_FILE_PATTERN))


def read_all_unihan_files(base_path=UNIHAN_BASE_PATH):
    file_paths = list_unihan_file_paths(base_path)
    df = pandas.concat([read_unihan_file(path) for path in file_paths])
    df.description = df.description.astype(str)
    df.reset_index(inplace=True, drop=True)
    return df


# ------------------------
# HSK
# ------------------------


def read_hsk_file(path):
    hsk_level = pathlib.Path(path).name.lstrip("hsk").rstrip(".txt")
    with open(path, "r") as file:
        content = file.read().strip()
        characters = [character for character in content]
        dataframe = pandas.DataFrame(characters, columns=["glyph"])
        dataframe.loc[:, "hsk_level"] = int(hsk_level)
        dataframe.hsk_level = dataframe.hsk_level.astype("Int64")
        return dataframe


def list_hsk_file_paths(base_path=HSK_BASE_PATH):
    return sorted(pathlib.Path(base_path).glob(HSK_FILE_PATTERN))


def read_all_hsk_files(base_path=HSK_BASE_PATH):
    file_paths = list_hsk_file_paths(base_path)
    return pandas.concat([read_hsk_file(path) for path in file_paths])


def merge_unihan_hsk(dataframe, hsk_table):
    return dataframe.merge(hsk_table, how="left", on="glyph")
