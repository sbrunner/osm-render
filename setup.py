# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = (
    open(os.path.join(here, 'README.rst')).read()
)

install_requires = [
    'tilecloud-chain',
]

setup_requires = [
]
tests_require = [
]

setup(
    name='osm-render',
    version='0.1',
    description="""
Tools to generates tiles on OSM data.
""",
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
    ],
    author='Stéphane Brunner',
    author_email='stephane.brunner@camptocamp.com',
    url='http://github.com/sbrunner/osm-render',
    license='BSD',
    keywords='gis tilecloud chain',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
