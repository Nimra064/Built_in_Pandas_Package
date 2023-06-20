from setuptools import setup, find_packages

setup(
    name='Pandas_package',
    version='0.1',
    packages=find_packages(),
    description='Built in Pandas package',
    author='Nimra Shahzadi',
    author_email='mehernimra064@gmail.com',
    url='https://github.com/Nimra064/Builtin_Pandas_Package',
    install_requires=[
        'requests>=2.26.0',
    ],
)
