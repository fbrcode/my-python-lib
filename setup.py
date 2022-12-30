from setuptools import find_packages, setup

setup(
    name="lib",
    packages=find_packages(include=["lib"]),
    version="0.1.0",
    description="My first Python library",
    author="Me",
    license="MIT",
    install_requires=[],
    tests_require=["pytest==7.2.0"],
    test_suite="tests",
)
