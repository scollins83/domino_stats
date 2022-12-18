#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = []
test_requirements = ['pytest>=3']

setup(
    author="Sara Collins",
    author_email='sara.collins0508@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="App to track scoring for Domino games, in a transparent \
    fashion with a clear interface. Helps with accusations of cheating during family domino games.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='domino_stats',
    name='Domino Stats',
    packages=find_packages(include=['domino_stats', 'domino_stats.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/scollins83/domino-stats',
    version='0.0.1',
    zip_safe=False,
)
