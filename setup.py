from setuptools import setup, find_packages
from typing import List

# def get_requirements(path="requirements.txt"):
#     with open(path) as f:
#         lines = f.read().splitlines()
#     return [line for line in lines if line and not line.startswith("#") and "-e" not in line]


HYPHEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="loan_default_analysis",
    version="0.1.0",
    author="M Mohsin",
    description="Data Science Project",
    packages=find_packages(),
    install_requires=get_requirements(),
)
