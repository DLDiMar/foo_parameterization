# Foo Parameterization Tool - Development Guide

## Introduction

Welcome to the development guide for the Foo Parameterization Tool. This document provides guidelines and instructions for developers who want to contribute to the project. 

## Getting Started

### Prerequisites

Ensure you have the following software installed on your development machine:

- Python 3.6 or higher
- `pip` (Python package installer)
- Git

### Setting Up the Development Environment

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/foo_param.git
    cd foo_param
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - **On Windows:**

        ```sh
        venv\Scripts\activate
        ```

    - **On macOS and Linux:**

        ```sh
        source venv/bin/activate
        ```

4. **Install the Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

## Coding Standards

### Style Guide

We follow the PEP 8 style guide for Python code. You can use tools like `flake8` to check your code for compliance.

### Docstrings

Use docstrings to document your functions and classes. Follow the PEP 257 conventions for docstrings.

### Type Annotations

Use type annotations to specify the expected types of function arguments and return values.

## Testing

### Running Tests

We use `pytest` for testing. To run the tests, execute the following command:

```sh
pytest
```

### Writing Tests

- Place your test files in the tests directory.
- Use descriptive names for your test functions.
- Ensure that each function tests a single piece of functionality.

See current tests in the `src/tests` directory for AAA formated examples.

## Contributing

### Submitting Changes

1.) Fork the Repository: Fork the repository on GitHub and clone your fork
2.) Create a Feature Branch:
    ```sh
    git checkout -b feature/your-feature
    ```
3.) Commit Your Changes: Follow the commit message conventions and ensure your code is well-documented and tested
4.) Push to your Fork
    ```sh
    git push origin feature/your-feature
    ```
5.) Create a Pull Request: Create a pull request on GitHub from your feature branch to the main branch of the original repository.

### Review Pull Requests

- Ensure the code follows the coding standards and style guide.
- Check for adequate test coverage.
- Provide constructive feedback.

## Contact

For any questions or suggestions, please contact:
- Dominic DiMarco
- Dominic.L.DiMarco@gmail.com