from setuptools import setup, find_packages
setup(
    name='SimpleVectors',
    version='0.1.0',
    packages=find_packages(),
    test_suite='tests',
    author='Sssspppuud',
    description='A Python package for some simplevector operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_vector_package',
    license='MIT',
)