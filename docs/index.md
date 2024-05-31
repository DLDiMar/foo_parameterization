# Foo Parameterization Tool

## Overview

The Foo Parameterization Tool is a Python package designed to calculate the volume of a sphere using the Foo et al. parameterization method. This package provides both a command-line interface (CLI) and a graphical user interface (GUI) to facilitate user interactions. The tool also includes visualization features to display the cross-section of the calculated sphere.

## Features

- Calculate the volume of a sphere given its radius.
- Command-line interface for quick calculations.
- Graphical user interface for user-friendly input.
- Logging of results to a CSV file.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Using a Virtual Environment

1. **Clone the Repository**

    ```sh
    git clone https://github.com/DLDiMar/foo_parameterization.git
    cd foo_parameterization
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

4. **Install the Dependencies and Foo et al. Program**

    ```sh
    pip install .
    ```

## Usage

See `usage.md` for details on using the CLI or UI tools.