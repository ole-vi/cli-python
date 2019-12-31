from setuptools import setup, find_packages

setup(
    name="treehouses-cli",
    version="1.1",
    packages=find_packages(),
    install_requires=["click"],
    extras_require={
        "develop": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "cli = cli.treehouses:cli",
        ],
    }
)
