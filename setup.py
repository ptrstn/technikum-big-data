from setuptools import setup


setup(
    name="bigchina",
    version="0.0.1",
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
        "setup",
    ],
    entry_points={"console_scripts": ["bigchina=bigchina.__main__:main"]},
)
