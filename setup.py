from __future__ import absolute_import

from setuptools import setup, find_packages
from io import open

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vresutils_Draworld',
    author='Jonas Hoersch (KIT,FIAS), David Schlachtberger (FIAS), Sarah Becker (FIAS)',
    author_email='contact@draworld.org',
    description='Varying Renewable Energy System Utilities',
    long_description=long_description,
    url='https://github.com/Shuwei-zhang/vresutils',
    license='GPLv3',
    packages=find_packages(exclude=['doc', 'test']),
    use_scm_version={'write_to': 'vresutils/version.py'},
    setup_requires=['setuptools_scm'],
    install_requires=['countrycode', 'fiona', 'matplotlib',
                      'memory_profiler',
                      'networkx>=2', 'numpy', 'pandas>=0.19.0',
                      'pyomo', 'scipy', 'pyproj', 'pyshp', 'rasterio>=1.0',
                      'shapely', 'six'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ])
