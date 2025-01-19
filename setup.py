from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirements(path:str)-> List[str]:
    """Get the requirements from the file"""
    with open(path) as f:
        requirements = f.read().splitlines()
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.1",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")

)