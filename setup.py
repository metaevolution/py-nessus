#!/usr/bin/env python

from distutils.core import setup

setup(name="pynessus-api",
      version='1.1',
      description='Simple python client for Nessus 5.x',
      author='Brandon Archer',
      author_email='m37a11@gmail.com',
      packages=['pynessus-api'],
      scripts=['scripts/nessus-client']
    )
    
