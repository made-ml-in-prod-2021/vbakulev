from setuptools import find_packages, setup

setup(
    name="src",
    packages=find_packages(),
    version="0.1.0",
    description="ML project",
    author="Vladimir Bakulev",
    install_requires=[
        "python-dotenv>=0.5.1",
        "scikit-learn==0.24.1",
        "dataclasses>=0.6",
        "pyyaml>=3.9",
        "marshmallow-dataclass==8.3.0",
        "pandas==1.1.5",
    ],
)
