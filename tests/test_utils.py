import numpy
import pandas

from bigchina.utils import rearrange_columns


def test_rearrange_columns():
    df = pandas.DataFrame(numpy.random.randn(6, 4), columns=list("ABCD"))
    df = rearrange_columns(df, ["B", "C"])
    assert list(df) == ["B", "C", "A", "D"]
