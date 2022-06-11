from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Vishal Thakur",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="astrovishalthakur@gmail.com",
    url="https://github.com/astrovishalthakur/Simple-DVC-Project",
    # package_dir={"":"src"}, in this line, empty key makes src source package which we don't want.
    # packages=find_packages(where="src"),
    packages = ["src"],
    license="GNU",
    python_requires=">=3.6",
    install_requires=[
        "dvc",
        "dvc[gdrive]",
        "dvc[s3]",
        "pandas",
        "scikit-learn"
    ]
)