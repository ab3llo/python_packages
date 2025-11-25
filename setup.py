from setuptools import setup    

setup(name='package',
    version='1.0.0',
    description='Example for creating your own packages',
    author='Bob the builder',
    author_email='bob_builder@gmail.com',
    packages=['package'], # list the location of all the init files in our package
    install_requires=[])