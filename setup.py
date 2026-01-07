from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    author="Your Name",
    author_email="yourmail@gmail.com",
    description="A simple Python package",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas"
    ],
    python_requires=">=3.7",
)
