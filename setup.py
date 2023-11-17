from setuptools import setup, find_packages

setup(
    name='etl-process',
    version='0.1.0',
    author='David Cannan',
    author_email='Cdaprod@Cdaprod.dev',
    description='A Python package for ETL processes with code context analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourpackagename',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        # e.g., 'requests', 'numpy'
        'asyncio',
        'ast',
        'tokenize'
    ],
    classifiers=[
        # Classifiers help users find your project by categorizing it.
        # For a list of valid classifiers, see https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)