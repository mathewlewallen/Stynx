from setuptools import setup, find_packages

setup(
    name="stynx",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "lark-parser>=0.11.3"
    ],
    entry_points={
        "console_scripts": [
            "stynx=stynx.main:main"
        ]
    },
)
