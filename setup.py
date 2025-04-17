from setuptools import setup, find_packages

setup(
    name="devtools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama~=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "devtools = devtools.cli:main",
        ],
    },
    author="Alexandre Desfossés",
    description="A developer utility toolbelt CLI",
)
