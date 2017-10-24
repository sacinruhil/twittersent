from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='twittersent',
    version=__version__,
    description='A python package to analyse the tweets and extract meaning from the data, can be installed with pip.',
    long_description=long_description,
    url='https://github.com/shekhar09/twittersent',
    download_url='https://github.com/shekhar09/twittersent/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: BSD License',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Shekhar Jha',
    install_requires=['twitter', 'seaborn', 'pandas', 'textblob'],
    dependency_links=dependency_links,
    author_email='shekhar09jha@gmail.com'
)