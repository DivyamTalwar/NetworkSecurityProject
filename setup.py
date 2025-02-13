from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() #to read each line
            for line in lines:
                requirement=line.strip() #remove all the whitespaces from each line
                if requirement and requirement!= '-e .': #ignore whitespace and -e
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="The Divyam Talwar",
    author_email="divyamtalwar15@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)