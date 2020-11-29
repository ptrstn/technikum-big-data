from bigchina.data import read_all_unihan_files, read_all_hsk_files
from bigchina.transform import (
    spread_unihan,
    extract_encode_glyph_columns,
    split_radical_additional_strokes_column,
    merge_unihan_hsk,
)


def load_data():
    print("Reading unihan files...")
    unihan = read_all_unihan_files()

    print("Spreading Unihan columns...")
    unihan = spread_unihan(unihan)
    print("Encoding Unicode notations...")
    unihan = extract_encode_glyph_columns(unihan)
    print("Splitting radical column...")
    unihan = split_radical_additional_strokes_column(unihan)

    print("Reading HSK files...")
    hsk_table = read_all_hsk_files()

    print("Merging Unihan with HSK dataframe...")
    return merge_unihan_hsk(unihan, hsk_table=hsk_table)
