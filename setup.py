from setuptools import find_packages,setup
from typing import List

HYPENN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        print(requirements)
        requirements=[req.replace("\n","") for req in requirements]


        if HYPENN_E_DOT in requirements:
            requirements.remove(HYPENN_E_DOT)

    return requirements


setup(name='mlproject',
      version='0.0.1',
      author='Rakesh sharma',
      author_email='en.rakeshsharma@gmail.com',
      packages=find_packages(),
      install_requires=get_requirments('requirements.txt'))