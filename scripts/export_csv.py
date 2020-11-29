# This script loads in the Unihan data, transforms it and merges it with the HSK data
# The resulting dataframe is then exported as data/unihan.csv

from bigchina.data import read_all_unihan_files, read_all_hsk_files
from bigchina.transform import (
    split_radical_additional_strokes_column,
    spread_unihan,
    extract_encode_glyph_columns,
    merge_unihan_hsk,
)
from bigchina.utils import rearrange_columns

print("Reading unihan files...")
dataframe = read_all_unihan_files()

print("Spreading Unihan columns...")
dataframe = spread_unihan(dataframe)
print("Encoding Unicode notations...")
dataframe = extract_encode_glyph_columns(dataframe)
print("Splitting radical column...")
dataframe = split_radical_additional_strokes_column(dataframe)


print("Reading HSK files...")
hsk_table = read_all_hsk_files()
print("Merging Unihan with HSK dataframe...")
dataframe = merge_unihan_hsk(dataframe, hsk_table=hsk_table)

dataframe.sort_values(
    ["hsk_level", "kFrequency", "additional_strokes", "radical"], inplace=True
)


desired_columns = [
    "glyph",
    "unicode",
    "kDefinition",
    "radical",
    "additional_strokes",
    "simplified_radical_indicator",
    "simplified_variant",
    "traditional_variant",
    "semantic_variant",
    "specialized_variant",
    "z_variant",
    "spoofing_variant",
    "compatibility_variant",
    "kTotalStrokes",
    "kFrequency",
    "hsk_level",
    "kGradeLevel",
    "kMandarin",
    "kHanyuPinlu",
    "kHanyuPinyin",
    "kCantonese",
    "kHangul",
    "kKorean",
    "kJapaneseKun",
    "kJapaneseOn",
    "kVietnamese",
    "kTang",
    "kTGHZ2013",
    "kXHC1983",
    "kRSAdobe_Japan1_6",
    "kRSKangXi",
    "kRSUnicode",
    "kSemanticVariant",
    "kSimplifiedVariant",
    "kSpecializedSemanticVariant",
    "kSpoofingVariant",
    "kTraditionalVariant",
    "kZVariant",
    "kAccountingNumeric",
    "kOtherNumeric",
    "kPrimaryNumeric",
]

dataframe = rearrange_columns(dataframe, desired_columns)

path = "data/unihan.csv"
dataframe.to_csv(path, sep="\t", index=False)
print(f"Exported dataframe to '{path}'")
