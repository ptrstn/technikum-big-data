from setuptools import setup


setup(
    name="bigchina",
    version="0.0.2",
    url="http://github.com/ptrstn/technikum-big-data",
    packages=["bigchina"],
    install_requires=[
        "requests",
        "pandas",
        "pyprojroot",
        "jupyter",
        "ipython",
        "matplotlib",
        "plotnine",
        "pynlpir",
        "wikipedia",
        "srt",
    ],
    entry_points={"console_scripts": ["bigchina=bigchina.__main__:main"]},
)
