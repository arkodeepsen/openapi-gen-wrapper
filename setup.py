from setuptools import setup, find_packages

setup(
    name="openapi-gen-wrapper",
    version="0.1.0",
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
    long_description=open('README.md').read(), # Detailed description from README file
    long_description_content_type="text/markdown",  # The format of your README
    url="https://github.com/arkodeepsen/openapi-gen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
