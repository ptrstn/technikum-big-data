from bigchina.data import read_all_unihan_files, read_all_hsk_files, download_unihan_zip
from bigchina.transform import (
    merge_unihan_hsk,
    spread_unihan,
    extract_encode_glyph_columns,
    split_radical_additional_strokes_column,
)


def test_transformation():
    download_unihan_zip()
    unihan = read_all_unihan_files()
    unihan = spread_unihan(unihan)
    unihan = extract_encode_glyph_columns(unihan)
    unihan = split_radical_additional_strokes_column(unihan)
    hsk = read_all_hsk_files()
    merge_unihan_hsk(unihan, hsk)
