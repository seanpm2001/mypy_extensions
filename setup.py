from setuptools import setup

version = '1.0.0-dev'
description = 'Experimental type system extensions for programs checked with the mypy typechecker.'
long_description = '''
Mypy Extensions
===============

The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.
'''.lstrip()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Topic :: Software Development',
]

setup(
    name='mypy_extensions',
    version=version,
    description=description,
    long_description=long_description,
    author='The mypy developers',
    author_email='jukka.lehtosalo@iki.fi',
    url='https://github.com/python/mypy_extensions',
    license='MIT License',
    py_modules=['mypy_extensions'],
    classifiers=classifiers,
)
