from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of requirements.
    """
    HYPHEN_E_DOT = '-e .'
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [r.replace('\n', '') for r in requirments]

    if HYPHEN_E_DOT in requirments:
        requirments.remove(HYPHEN_E_DOT)

    return requirments

setup(
    name='mlproject',
    version='0.0.1',
    author='Sukruth',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)