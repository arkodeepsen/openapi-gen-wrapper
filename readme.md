# OpenAPI Gen Wrapper
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
