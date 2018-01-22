from setuptools import find_packages, setup

VERSION = "0.5.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/blank.svg
    :target: https://pypi.python.org/pypi/pinax-pages/

===================
Pinax Pages
===================
.. image:: https://img.shields.io/pypi/v/pinax-pages.svg
    :target: https://pypi.python.org/pypi/pinax-pages/
\
.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-pages.svg
    :target: https://circleci.com/gh/pinax/pinax-pages
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-pages.svg
    :target: https://codecov.io/gh/pinax/pinax-pages
.. image:: https://img.shields.io/github/contributors/pinax/pinax-pages.svg
    :target: https://github.com/pinax/pinax-pages/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-pages.svg
    :target: https://github.com/pinax/pinax-pages/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-pages.svg
    :target: https://github.com/pinax/pinax-pages/pulls?q=is%3Apr+is%3Aclosed
\
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/
\

A light weight CMS born out of Symposion

Supported Django and Python Versions
------------------------------------
+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a Django pages app",
    name="pinax-pages",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="https://github.com/pinax/pinax-pages/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pages": []
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    install_requires=[
        "django-appconf>=1.0.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
