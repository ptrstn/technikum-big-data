import pathlib
from zipfile import ZipFile

import pandas
import requests

UNIHAN_ZIP_URL = "https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip"
UNIHAN_BASE_PATH = pathlib.Path("data", "unihan")
UNIHAN_FILE_PATTERN = "Unihan_*.txt"


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


def download_unihan_zip(base_path=UNIHAN_BASE_PATH, url=UNIHAN_ZIP_URL, quiet=False):
    file_name = pathlib.Path(url).name
    file_path = pathlib.Path(base_path, file_name)
    download_file(url, file_path, quiet=quiet)
    extract_zip(file_path, base_path, quiet=quiet)


def read_unihan_file(path):
    column_names = ["unicode", "field", "description"]
    return pandas.read_table(path, names=column_names, comment="#")


def list_unihan_file_paths(base_path=UNIHAN_BASE_PATH):
    return list(pathlib.Path(base_path).glob(UNIHAN_FILE_PATTERN))


def read_all_unihan_files(base_path=UNIHAN_BASE_PATH):
    file_paths = list_unihan_file_paths(base_path)
    df = pandas.concat([read_unihan_file(path) for path in file_paths])
    df.description = df.description.astype(str)
    df.reset_index(inplace=True, drop=True)
    return df
