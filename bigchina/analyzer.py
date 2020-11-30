import numpy
import pandas
import pynlpir
import srt
import wikipedia

pynlpir.open()


def segment_text(text) -> pandas.DataFrame():
    segments = pynlpir.segment(text)
    df = pandas.DataFrame(segments, columns=["segment", "characteristic"])
    df.segment = df.segment.str.strip()
    df = df[df.segment != ""]
    df["is_punctuation"] = df.characteristic == "punctuation mark"
    df.loc[df["is_punctuation"], "sentence"] = list(
        range(1, len(df.loc[df["is_punctuation"]]) + 1)
    )
    df.iloc[0, df.columns.get_loc("sentence")] = 0
    df.sentence.fillna(method="ffill", inplace=True)
    df.sentence = df.sentence.astype("int64")
    df["sentence_word_id"] = df.groupby("sentence").cumcount()
    return df


def segment_wikipedia_article(title, language="zh"):
    wikipedia.set_lang(language)
    article = wikipedia.page(title)
    return segment_text(article.content)


def segment_subtitle_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return segment_subtitle(file.read())


def segment_subtitle(text):
    return segment_text(
        ". ".join(
            [
                element.content
                for element in list(srt.parse(text))
                if element.content.isprintable()
            ]
        )
    )


def rolling_unique_count(dataframe, column):
    unique_name = f"rolling_unique_{column}_count"
    dataframe = dataframe.reset_index(drop=True)
    factorized = pandas.Series(dataframe[column].factorize()[0])
    dataframe[unique_name] = factorized.expanding().apply(lambda x: len(numpy.unique(x))).astype("int64")
    return dataframe
