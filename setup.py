
   
import re
from setuptools import setup, find_packages

#
# this package has extra requirements, check README for details
#

def find_version(file_path: str) -> str:
    version_file = open(file_path).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if not version_match:
        raise RuntimeError(f"Unable to find version string in {file_path}")
    return version_match.group(1)

def load_requirements(filename: str):
    with open(filename) as f:
        return [x.strip() for x in f.readlines() if "-r" != x[0:2]]

setup(name='dust3r', 
    license='Proprietary', 
    url='https://github.com/naver/dust3r',

    version=find_version("dust3r/__init__.py"), 
    packages=find_packages(),
)