[![Actions Status](https://github.com/ptrstn/technikum-big-data/workflows/Python%20package/badge.svg)](https://github.com/ptrstn/technikum-big-data/actions)
[![codecov](https://codecov.io/gh/ptrstn/technikum-big-data/branch/master/graph/badge.svg?token=XrchtoPede)](https://codecov.io/gh/ptrstn/technikum-big-data)

# Big Data & Machine Learning!

This project deals with the analysis of the Unihan data set.
Unihan is an effort of the authors of the Unicode standard to standardize the so-called "Han characters", which are used in China, Taiwan, Hong Kong, Japan, Singapore and have also been used in countries like Korea and Vietnam.

## Questions

Possible questions that can be answered and visualized are the following:

- Which are the most frequently used Radicals?
- Which are the most frequently used Characters?
- Is a trend visible?
- Does the Chinese Language Exam HSK cover the most frequently used words?
- Are certain words together in a sentence?
- Which are the most commonly used words in chinese Music?
- Which are the most commonly used words in chinese News Paper?
- Which are the most commonly used words in chinese Movies?
- Are there Hapax legomenon for a certain area (words that are used only once)?

## Requirements

- Python 3.8+

## Installation

```bash
git clone https://github.com/ptrstn/technikum-big-data
cd technikum-big-data
pip install -e .
```

## Run

```bash
bigchina
```

```
Downloading Dataset...
Downloading https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip to data/unihan/Unihan.zip...
Extracting data/unihan/Unihan.zip to data/unihan...
Reading Dataset...
         unicode              field      description
0         U+3402           kJIS0213          1,14,03
1         U+3406           kJIS0213          2,01,13
2         U+340C              kKPS1             3451
3         U+341C              kKPS1             345F
4         U+3425              kKPS1             346A
...          ...                ...              ...
1356823  U+2F9D0  kRSAdobe_Japan1_6  C+14068+149.7.9
1356824  U+2F9DE  kRSAdobe_Japan1_6  C+20066+159.7.3
1356825  U+2F9DF  kRSAdobe_Japan1_6  C+14069+159.7.9
1356826  U+2F9F4  kRSAdobe_Japan1_6  C+15269+45.3.12
1356827  U+2FA0E          kRSKangXi            196.9

[1356828 rows x 3 columns]
```