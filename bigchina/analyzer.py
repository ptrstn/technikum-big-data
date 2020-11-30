import pandas
import pynlpir
import wikipedia

pynlpir.open()


def segment_text(text) -> pandas.DataFrame():
    segments = pynlpir.segment(text)
    df = pandas.DataFrame(segments, columns=["segment", "characteristic"])
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
