# This script loads in the Unihan data, transforms it and merges it with the HSK data
# The resulting dataframe is then exported as data/unihan.csv

from bigchina import load_data
from bigchina.utils import rearrange_columns


dataframe = load_data()

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
