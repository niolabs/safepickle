import sys
import re
from setuptools import setup, find_packages

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

with open('safepickle/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='safepickle',
    description="An alternative to using Python's pickle",
    keywords=['safepickle'],
    license='Apache 2.0',
    version=version,
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),

    install_requires=[],
    tests_require=['pytest', 'pytest-cov'],
    cmdclass={'test': PyTest},

    author='n.io',
    author_email='info@n.io',
    url='http://n.io'
)
