# Foo Parameterization Tool - Usage Guide

## Introduction

The Foo Parameterization Tool is a versatile software package designed to calculate the volume of a sphere using the Foo et al. parameterization method. This guide will walk you through using both the command-line interface (CLI) and the graphical user interface (GUI) to perform calculations and visualize results.

## Initial Install

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
    pip install -r requirements.txt
    ```

You are ready to use either the CLI or GUI. See below for using each.

## Command-Line Interface (CLI)

### Running the CLI

To run the CLI, navigate to the root directory ('foo_parameterization') and run the following command**: 

```sh
foo_et_al_param
```

** If the command doesn't work, please use the following set of commands:
```sh
cd src/foo_param
python core.py
```
Or if using Python3, use `python3 core.py`

### Example
```sh
$ foo_et_al_param
Foo et al. Parameterization tool
Enter the radius of the sphere: 3
Enter the decimal precision for the volume: 3
The volume of the sphere with radius 3.0 is 113.097
Result added to csv file: csv_outputs\user-_results-2024-05-30 2024-05-30.csv
```

### Logging Results

Each calculation performed via the CLI is logged to a CSV file in the csv_outputs directory. The CSV file is named with the current date and time to ensure uniqueness.

## Graphical User Interface (GUI)

### Running the GUI

To run the GUI, navigate to the root directory ('foo_parameterization') and run the following command**:

```sh
foo_et_al_param_gui
```

** If the command doesn't work, please use the following set of commands:
```sh
cd src/foo_param
python run_gui.py
```
Or if using Python3, use `python3 run_gui.py`

This will open a window where you can input the radius and determine the volume.

### Using the GUI

1.) Enter the Radius: Type the radius of the sphere into the input box.
2.) Enter Decimal Precision: Specify the number of decimal places for the volume.
3.) Calculate and Visualize: Click the "Calculate Volume" button to see the results.

## Troubleshooting

### Common Issues

1.) Invalid Radius Input: Ensure the radius is a positive number.
2.) CSV Logging Issues: Make sure the csv_outputs directory exists and is writable.
3.) GUI Issues: Ensure all dependencies are installed and your Python environment is correctly set up.

