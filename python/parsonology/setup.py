from setuptools import setup
import sys

install_requires = ['six', 'toolz', 'pyrsistent']
if sys.version_info < (3, 5):
    install_requires.append('typing')

setup(name='parsonology',
      version='0.0.0',
      description='A dumb parser',
      url='http://github.com/lucaswiman/simple-parser',
      author='Lucas Wiman   ',
      author_email='lucas.wiman@gmail.com',
      license='Apache 2.0',
      packages=['parsonology'],
      install_requires=install_requires,
      long_description='foo',
      zip_safe=False)
