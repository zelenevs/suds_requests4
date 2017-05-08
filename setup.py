from setuptools import setup


setup(
    name='suds_requests',
    version='0.3.1',
    description='A suds transport implemented with requests',
    long_description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='jmrosal@crosal-research.com',
    py_modules=['suds_requests'],
    install_requires=['requests', 'suds-py3'],
    license='MIT',
    url='https://github.com/armooo/suds_requests',
)
