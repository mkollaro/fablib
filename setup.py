from distutils.core import setup

setup(
    name='fabric-wrap',
    version='0.0.1',
    author='Martina Kollarova',
    author_email='mkollaro@gmail.com',
    url='http://pypi.python.org/pypi/fabric-wrap/',
    packages=['fabric-wrap'],
    license='LICENSE',
    description='Wrappers around Fabric for nicer usage as a library',
    long_description=open('README.md').read(),
    install_requires=[
        'fabric',
    ],
)
