# Foo Parameterization Tool

## Overview

The Foo Parameterization Tool is a Python package designed to calculate the volume of a sphere using the Foo et al. parameterization method. This package provides both a command-line interface (CLI) and a graphical user interface (GUI) to facilitate user interactions. The tool also includes visualization features to display the cross-section of the calculated sphere and logs results to a CSV file.

## Features

- Calculate the volume of a sphere given its radius.
- Command-line interface for quick calculations.
- Graphical user interface for user-friendly input and visualization.
- Visualization of the sphere's cross-section.
- Logging of results to a CSV file.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)

### Using a Virtual Environment

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

### Command-Line Interface

To calculate the volume of a sphere using the CLI, run the following command:

```sh
python src/foo_param/core.py <radius>
```

Replace `<radius>` with the radius of the sphere you want to calculate the volume for. For example, at the base level of this project:

```sh
python src/foo_param/core.py
```

### Graphical User Interface (GUI)

To use the GUI, run the following command at the base level of this project:

```sh
python src/foo_param/gui.py
```

This will open a window where you can input the radius and visualize the resulting sphere's cross-section.

## Documentation

For more detailed documentation, please refer to the following files:

- [Development Guide](docs/development.md)
- [Usage Guide](docs/usage.md)
- [Index](docs/index.md)


## Contact

For any questions or suggestions, please contact:
- Dominic DiMarco
- Dominic.L.DiMarco@gmail.com