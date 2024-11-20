import os
from setuptools import setup, find_packages

import os
from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = '''# OpenAPI Gen Wrapper
[![Upload Python Package](https://github.com/arkodeepsen/openapi-gen-wrapper/actions/workflows/python-publish.yml/badge.svg)](https://github.com/arkodeepsen/openapi-gen-wrapper/actions/workflows/python-publish.yml)
## Description

A Python wrapper for generating OpenAPI specifications from routes in a Python project.

## Installation

```bash
pip install openapi-gen-wrapper
```

## Usage
Here’s how you can use the wrapper:

```python
from openapi_gen_wrapper import generate_openapi_spec
```

# Example usage
```
generate_openapi_spec(routes=["/hello", "/goodbye"])
```
License
```
MIT License
```
'''

setup(
    name="openapi-gen-wrapper",
    version="0.1.1",
    packages=find_packages(),
    install_requires=["click", "pyyaml"],
    entry_points={
        'console_scripts': [
            'openapi-gen=src.cli:main'
        ]
    },
    author="Arkodeep Sen",
    author_email="arkodeepsen72@gmail.com.com",
    description="A Python tool for generating OpenAPI specs",  # Short description
    long_description=long_description,
    long_description_content_type="text/markdown",  # The format of your README
    url="https://github.com/arkodeepsen/openapi-gen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
