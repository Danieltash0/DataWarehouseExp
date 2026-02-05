# setup.py
from setuptools import setup, find_packages

setup(
    name="DataWarehouseExp",
    version="0.1.0",
    packages=find_packages(),  # This finds all packages automatically
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.20.0",
        "sqlalchemy>=2.0.0",
        "flask>=2.0.0",
        "plotly>=5.0.0",
        "dash>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
)