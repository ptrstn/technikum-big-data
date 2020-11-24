import pandas

from bigchina.utils import extract_encode_glyphs


def spread_unihan(dataframe: pandas.DataFrame) -> pandas.DataFrame:
    dataframe = dataframe.pivot(index="unicode", columns="field", values="description")
    dataframe.reset_index(inplace=True)
    return dataframe


def extract_encode_glyph_columns(dataframe):
    column_names = {
        "unicode": "glyph",
        "kSimplifiedVariant": "simplified_variant",
        "kTraditionalVariant": "traditional_variant",
        "kSemanticVariant": "semantic_variant",
        "kSpecializedSemanticVariant": "specialized_variant",
        "kZVariant": "z_variant",
        "kSpoofingVariant": "spoofing_variant",
        "kCompatibilityVariant": "compatibility_variant",
    }

    for old_name, new_name in column_names.items():
        dataframe[new_name] = dataframe[old_name].apply(extract_encode_glyphs)

    return dataframe


def assure_two_columns(dataframe):
    if len(list(dataframe)) == 1:
        dataframe[1] = None
    return dataframe


def _split_kRSUnicode_column(dataframe):
    splitted = dataframe.kRSUnicode.str.split(" ", expand=True)
    return assure_two_columns(splitted)


def _split_radical_stroke_column(dataframe):
    splitted = dataframe.radical_stroke.str.split(".", expand=True)
    return assure_two_columns(splitted)


def _split_radical_column(dataframe):
    splitted = dataframe.radical.str.split("'", expand=True)
    splitted = assure_two_columns(splitted)
    splitted.loc[~splitted[1].isnull(), 1] = True
    splitted.loc[splitted[1].isnull(), 1] = False
    return splitted


def split_radical_additional_strokes_column(dataframe):
    dataframe[["radical_stroke", "second_radical_stroke"]] = _split_kRSUnicode_column(
        dataframe
    )

    dataframe[["radical", "additional_strokes"]] = _split_radical_stroke_column(
        dataframe
    )

    dataframe[["radical", "simplified_radical_indicator"]] = _split_radical_column(
        dataframe
    )

    dataframe.drop(["radical_stroke", "second_radical_stroke"], axis=1, inplace=True)
    dataframe.radical = dataframe.radical.astype(int)
    dataframe.additional_strokes = dataframe.additional_strokes.astype(int)

    return dataframe
