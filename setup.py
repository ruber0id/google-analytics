import codecs

from setuptools import find_packages, setup

setup(name='googleanalytics',
    description='A wrapper for the Google Analytics API.',
    long_description=codecs.open('README.rst', 'r', 'utf-8').read(),
    author='Stijn Debrouwere',
    author_email='stijn@debrouwere.org',
    url='https://github.com/debrouwere/google-analytics/',
    download_url='http://www.github.com/debrouwere/google-analytics/tarball/master',
    version='0.26.0',
    license='ISC',
    packages=find_packages(),
    keywords='data analytics api wrapper google',
    scripts=[
        'bin/googleanalytics'
    ],
    include_package_data=True,
    install_requires=[
        'oauth2client==1.5.2',
        'google-api-python-client==1.4.2',
        'python-dateutil',
        'addressable>=1.4.2',
        'inspect-it>=0.3.2',
        'werkzeug>=0.10',
        'keyring>=5.3',
        'click>=6',
        'pyyaml>=3',
        'prettytable>=0.7',
        'colorama>=0.3',
        'snakify>=1.1',
    ],
    test_suite='googleanalytics.tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    )
