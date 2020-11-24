from .transform import spread_unihan
from .data import download_unihan_zip, read_all_unihan_files


def main():
    print(f'Downloading Dataset...')
    download_unihan_zip()
    print(f'Reading Dataset...')
    df = read_all_unihan_files()
    print(df)
    df = spread_unihan(df)
    print(df)


if __name__ == '__main__':
    main()
