from setuptools import setup, find_packages
setup(
    name='syncwerk-server-python',
    version='20181227',
    author='Syncwerk GmbH',
    author_email='support@syncwerk.com',
    packages=find_packages(exclude=["Makefile.am", "*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://www.syncwerk.com',
    license='Apache 2.0',
    description='Server client',
    long_description='Client module to communicate with the Syncwerk file server',
    platforms=['any'],
    include_package_data=True,
)
