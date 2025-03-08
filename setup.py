from setuptools import setup, find_packages

setup(
    name="openlibrary_api",
    version="0.1.0",
    packages=find_packages(),
    requires=[
        "requests",
        "urllib",
        "json",
    ]
)