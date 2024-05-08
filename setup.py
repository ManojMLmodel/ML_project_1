from setuptools import find_packages, setup
from typing import List

REQUIREMENTS_FILE = "requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirement() -> List[str]:
    with open(REQUIREMENTS_FILE) as requirement_file:
        requirement_list = requirement_file.readlines()
    
    requirement_list = [requirement_name.strip() for requirement_name in requirement_list]

    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    
    return requirement_list

setup(name="cost_prediction",
      version="0.0.1",
      description="Data science project",
      author="Manoj Malavkar",
      author_email="malavkar.manoj@gmail.com",
      packages=find_packages(),
      install_requires=get_requirement(),
      )

