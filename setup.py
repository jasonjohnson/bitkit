from setuptools import setup

setup(
    name="bitkit",
    version="0.0.1",
    author="Jason Johnson",
    author_email="spligak@gmail.com",
    packages=[
        "bitkit"
    ],
    entry_points={
        "console_scripts": [
            "bitkit = bitkit.cli:main"
        ]
    },
    zip_safe=False
)
