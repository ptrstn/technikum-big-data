from .transform import spread_unihan, extract_encode_glyph_columns, split_radical_additional_strokes_column
from .data import download_unihan_zip, read_all_unihan_files


def main():
    print(f'Downloading Dataset...')
    download_unihan_zip()
    print(f'Reading Dataset...')
    df = read_all_unihan_files()
    print(df)
    print(f'Spreading Columns...')
    df = spread_unihan(df)
    print(df)
    print(f'Encoding Columns...')
    df = extract_encode_glyph_columns(df)
    print(df)
    print(f'Splitting Radical Column...')
    df = split_radical_additional_strokes_column(df)
    print(df)


if __name__ == '__main__':
    main()
