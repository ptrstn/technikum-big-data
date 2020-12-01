from setuptools import setup


setup(
    name="bigchina",
    version="0.0.3",
    url="http://github.com/ptrstn/technikum-big-data",
    packages=["bigchina"],
    install_requires=[
        "requests",
        "pandas>1.1",
        "pyprojroot",
        "jupyter",
        "ipython",
        "matplotlib>3.3",
        "plotnine",
        "pynlpir",
        "wikipedia",
        "srt",
    ],
    entry_points={"console_scripts": ["bigchina=bigchina.__main__:main"]},
)
