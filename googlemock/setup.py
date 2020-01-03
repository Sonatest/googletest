from setuptools import setup

setup(
    name='googlemock',
    version='1.8.1',
    description='Generator of C++ Mock Class',
    url='https://github.com/Sonatest/googletest/scripts/generator',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='googlemock mock',
    packages=['googlemock'],
    package_dir={'googlemock': 'googlemock/generator/cpp'},
)
