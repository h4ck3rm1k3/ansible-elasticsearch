#!/usr/bin/env python

from distutils.core import setup
from distutils.cmd import Command

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        raise SystemExit(
            subprocess.call(['nosetests',
                             '--verbosity=999']))

setup(name='ansible-elasticsearch',
      version='1.0',
      description='An Ansible role for installing ElasticSearch',
      author='Hector Castro',
      author_email='hectcastro@gmail.com',
      url='https://github.com/elasticsearch/cookbook-elasticsearch',
      requires=['ansible', 'nose'],
      data_files=[ ],
      cmdclass={
          'test': TestCommand
      }
  )
