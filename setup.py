from setuptools import setup


setup(
    name='suds_requests',
    version='1.0.0',
    description='A suds transport implemented with requests using suds-community',
    long_description=open('README.rst').read(),
    author='Jason Michalski',
    author_email='jmrosal@crosal-research.com',
    py_modules=['suds_requests'],
    install_requires=['requests', 'suds-community'],
    license='MIT',
    url='https://github.com/zelenevs/suds_requests4',
	python_requires='>=3.7',
)
