#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='fuo_explore',
    version='0.1.dev0',
    description='Music story.',
    author='Cosven',
    author_email='yinshaowen241@gmail.com',
    packages=find_packages(exclude=('tests*',)),
    package_data={
        },
    url='https://github.com/cosven/feeluown-explore',
    keywords=['feeluown', 'plugin', 'explore'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'feeluown>=3.7.7',
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'fuo.plugins_v1': [
            'explore = fuo_explore',
        ]
    },
)
