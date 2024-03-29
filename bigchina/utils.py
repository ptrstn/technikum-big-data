import re

import numpy

from bigchina.decorators import non_null_call


def extract_unicode_notations(text, join_on=" "):
    """
    Checks a text for existing unicode notations and returns only them
    """
    return join_on.join(re.findall(r"U\+[0-9A-F]+", text))


def _match_encode_unicode_notation(match):
    return encode_unicode_notation(match.group())


def encode_unicode_notations_in_text(text):
    """
    Encodes a Unicode notation into a human readable form.
    """
    return re.sub(r"U\+[0-9a-fA-F]+", _match_encode_unicode_notation, text)


def encode_unicode_notation(unicode_notation):
    """
    Encodes a ASCII-fied unicode notation ("U+" convention)

    :param unicode_notation: string like "U+2F08"
    :return: encoded unicode character like "人"
    """
    return chr(int(unicode_notation.replace("U+", ""), 16))


@non_null_call
def extract_encode_glyphs(value):
    glyphs = encode_unicode_notations_in_text(extract_unicode_notations(value))
    return glyphs if glyphs else numpy.nan


def rearrange_columns(dataframe, columns):
    """
    Sorts the columns in dataframe in the order of the columns list.
    Any remaining columns will appended in the previous order.
    """
    all_names = list(dataframe)
    remaining_names = [name for name in all_names if name not in columns]
    new_order = [*columns, *remaining_names]
    return dataframe[new_order]
