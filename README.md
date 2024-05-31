# Foo Parameterization Tool

## Overview

The Foo Parameterization Tool is a Python package designed to calculate the volume of a sphere using the Foo et al. parameterization method. This package provides both a command-line interface (CLI) and a graphical user interface (GUI) to facilitate user interactions. The tool also includes visualization features to display the cross-section of the calculated sphere and logs results to a CSV file.

## Features

- Calculate the volume of a sphere given its radius.
- Command-line interface for quick calculations.
- Graphical user interface for user-friendly input and visualization.
- Visualization of the sphere's cross-section.
- Logging of results to a CSV file.
- Can utilize as a Python library for integration with other projects.

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

4. **Install the Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

### Command-Line Interface

To calculate the volume of a sphere using the CLI, run the following command:

```sh
foo_et_al_param
```

### Graphical User Interface (GUI)

To use the GUI, run the following command at the base level of this project:

```sh
foo_et_al_param_gui
```

This will open a window where you can input the radius and visualize the resulting sphere's cross-section.

## Using as a Python Library

You can also use the Foo et al. Parameterization Tool as a Python library in your own projects. Here is an example of how to use it:

```python
from foo_param.models.input_model import InputModel
from foo_param.models.sphere_model import SphereModel
from foo_param.utils.csv_logger import log_result

# Create an input model and set parameters
input_model = InputModel()
input_model.sphere_input(radius=5, precision=2)

# Create a sphere model with the input parameters and calculate the volume
sphere_model = SphereModel(input_model.param1_value)
volume = sphere_model.calculate()
print(f"The volume of the sphere with radius {input_model.param1_value} is {volume:.{input_model.precision}f}")

# Log the result to a CSV file
csv_output = log_result("sphere", input_model.param1_name, input_model.param1_value, volume_output=volume)
print(f"Result added to CSV file: {csv_output}")
```

## Documentation

For more detailed documentation, please refer to the following files:

- [Development Guide](docs/development.md)
- [Usage Guide](docs/usage.md)
- [Index](docs/index.md)


## Contact

For any questions or suggestions, please contact:
- Dominic DiMarco
- Dominic.L.DiMarco@gmail.com