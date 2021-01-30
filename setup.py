import io
import setuptools

with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid19hd",
    version="1.0.0",
    author="Jeongbin Park",
    author_email="pjb7687@gmail.com",
    description="COVID-19 statistics in Heidelberg/RNK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pjb7687/covid19hd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "pdfminer.six",
        "numpy",
        "pandas",
    ]
)