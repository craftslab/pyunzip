#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

from pyunzip.cmd.version import VERSION


with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setuptools.setup(
    author='Jia Jia',
    author_email='angersax@sina.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    description='Streaming unzip utility',
    download_url='https://github.com/craftslab/pyunzip/archive/v%s.tar.gz' % VERSION,
    entry_points={'console_scripts': ['pyunzip=pyunzip.main:main']},
    include_package_data=True,
    install_requires=requirements,
    keywords=['streaming', 'unzip', 'utility'],
    license='Apache-2.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='pyunzip',
    packages=setuptools.find_packages(exclude=['examples', 'ez_setup', 'release', 'script', 'tests', 'tests.*']),
    package_data={'pyunzip': []},
    url='https://github.com/craftslab/pyunzip',
    version=VERSION,
    zip_safe=False)
