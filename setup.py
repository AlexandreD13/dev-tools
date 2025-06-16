from setuptools import setup, find_packages

setup(
    name="devtools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "colorama~=0.4.6",
        "setuptools~=78.1.0",
        "Flask~=3.1.0",
        "devtools~=0.1.0",
        "flask-cors~=5.0.1",
        "Faker~=37.1.0",
    ],
    entry_points={
        "console_scripts": [
            "devtools = devtools.cli:main",
        ],
    },
    author="Alexandre Desfossés",
    description="A developer utility toolbelt CLI",
)
