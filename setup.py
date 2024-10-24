import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Read requirements from requirements.txt
def read_requirements():
    requirements = []
    try:
        with open(HERE / "requirements.txt", encoding="utf-8") as req_file:
            for line in req_file:
                line = line.strip()
                if line and not line.startswith("#"):  # Skip empty lines and comments
                    requirements.append(line)
    except FileNotFoundError:
        print("Warning: requirements.txt not found")
    return requirements

# This call to setup() does all the work
setup(
    name="aift",  # package name
    version="0.2.1",  # Incremented version number
    author="c-tawayip",  # creator username
    author_email="chuangk.piyawat@gmail.com",  # email creator
    description="AI for Thai's Python Package",  # description
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AIforThai/aiforthai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    # packages=["aift"],
    include_package_data=True,
    install_requires=read_requirements(),
    packages=find_packages()
)