from setuptools import setup

setup(
	name='SuperHash',
    version='0.2b1',
    author='Philip Schleihauf',
    author_email='uniphil@gmail.com',
    license='GPLv3',
    description='Hash anything',
    long_description=open('README.md').read(),
    py_modules=['superhash'],
    test_requires=['stuf>=0.9.10'],
    url='https://github.com/uniphil/SuperHash',
    )
