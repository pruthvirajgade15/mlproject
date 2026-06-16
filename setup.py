from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path, 'r') as f:
        requirements = [line.strip() for line in f]
    return requirements




setup(
    name='mlproject',
    version='0.1',
    author='Prithviraj',
    author_email='pruthvirajgade2@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)                    