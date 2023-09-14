from setuptools import find_packages,setup  # find_packages help in find all the sub modules
from typing import List 

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:  
    requirements=[]
    with open(file_path) as file_obj:        
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]   #Removing /n, which is getting added while reading .txt file

        if HYPEN_E_DOT in requirements:              #Removes -e . from requirements.txt
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Yogesh',
    author_email='yogeshofficial19@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)



# To run the setup.py use python setup.py install

# -e . basically links the -r requirements. txt to setup.py so that  when we call the pip install -r requiremnts.txt it will run 
# setup.py by default