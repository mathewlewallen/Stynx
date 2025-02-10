from setuptools import setup, find_packages

setup(
    name="stynx",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "stynx=stynx.cli:main"
        ]
    },
)
