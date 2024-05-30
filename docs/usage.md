# Foo Parameterization Tool - Usage Guide

## Introduction

The Foo Parameterization Tool is a versatile software package designed to calculate the volume of a sphere using the Foo et al. parameterization method. This guide will walk you through using both the command-line interface (CLI) and the graphical user interface (GUI) to perform calculations and visualize results.

## Command-Line Interface (CLI)

### Running the CLI

To run the CLI, navigate to the `src/foo_param` directory and execute `core.py` with the desired radius as an argument.

```sh
python src/foo_param/core.py <radius>
```

Replace `<radius>` with the radius of the sphere you want to calculate the volume for. For example, at the base level of this project:

```sh
python src/foo_param/core.py
```

### Example
```sh
$ python .\src\foo_param\core.py
Enter the radius of the sphere: 3
Enter the decimal precision for the volume: 3
The volume of the sphere with radius 3.0 is 113.097
Result added to csv file: csv_outputs\user-_results-2024-05-30 2024-05-30.csv
```

### Optional Parameters

You can also specify optional parameters such as param2 and param3. The script will prompt you for these values if they are needed.

### Logging Results

Each calculation performed via the CLI is logged to a CSV file in the csv_outputs directory. The CSV file is named with the current date and time to ensure uniqueness.

## Graphical User Interface (GUI)

### Running the GUI

To run the GUI, navigate to the src/foo_param directory and execute gui.py.

```sh
python src/foo_param/gui.py
```
This will open a window where you can input the radius and visualize the resulting sphere's cross-section.

### Using the GUI

1.) Enter the Radius: Type the radius of the sphere into the input box.
2.) Enter Decimal Precision: Specify the number of decimal places for the volume.
3.) Calculate and Visualize: Click the "Calculate Volume" button to see the results.

## Troubleshooting

### Common Issues

1.) Invalid Radius Input: Ensure the radius is a positive number.
2.) CSV Logging Issues: Make sure the csv_outputs directory exists and is writable.
3.) GUI Issues: Ensure all dependencies are installed and your Python environment is correctly set up.

