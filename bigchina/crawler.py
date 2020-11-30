import pandas
import requests
import wikipedia

url_pattern = "https://pageviews.toolforge.org/topviews/yearly_datasets/{language}.wikipedia/{year}.json"

def crawl_wikipedia_articles(language = "zh", year=2019, max_rank = 10):
    url = url_pattern.format(language=language, year=year)
    json_response = requests.get(url).json()
    df = pandas.DataFrame(json_response)
    df["rank"] = df["rank"].astype("int64")
    df = df[df["rank"] <= max_rank]
    df.loc[:, "year"] = year

    print(f'Retrieving top {max_rank} {language} wikipedia pages of year {year}...')
    wikipedia.set_lang(language)
    df.loc[:, "article_content"] = df.article.apply(lambda title: wikipedia.page(title).content)
    return df