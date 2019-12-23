# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sipgateio-sendsms-python',
    version='0.1.0',
    description='A demonstration of how to send SMS using sipgate.io',
    long_description=readme,
    author='sipgate.io Team',
    author_email='io-team@sipgate.de',
    url='https://github.com/sipgate/sipgateio-sendsms-python',
    license=license,
    packages=find_packages(exclude=())
)
