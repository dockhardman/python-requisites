# Python Requisites

Python Requisites is a dynamic tool for the explicit declaration and analysis of dependencies in Python objects, streamlining the process of identifying and managing required elements in your code.

## Introduction

Python Requisites (or `python-requisites`) provides an intuitive way to analyze and declare the dependencies in Python objects like functions, classes, and modules. This tool is particularly useful for developers looking to gain better insight into their code's structure and dependencies.

## Features

- **Explicit Dependency Declaration**: Clearly outlines the dependencies within Python objects.
- **Streamlined Analysis**: Simplifies the process of identifying required arguments and dependencies in functions, classes, and modules.
- **Easy Integration**: Designed to seamlessly integrate with existing Python projects.

## Installation

You can install Python Requisites using pip:

```bash
pip install python-requisites
```

## Usage

To utilize Python Requisites in your project, simply import the module and pass your Python object for analysis.

```python
from requisites import analyze_dependencies

# Analyze dependencies of a function
dependencies = analyze_dependencies(my_function)
print(dependencies)
```
