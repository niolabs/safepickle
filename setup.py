import re
from setuptools import setup, find_packages

with open('safepickle/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='safepickle',
    description="An alternative to using Python's pickle",
    keywords=['safepickle'],
    version=version,
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),

    install_requires=[],
    tests_require=[],

    author='n.io',
    author_email='info@n.io',
    url='http://n.io'
)
