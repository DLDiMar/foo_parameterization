from models.sphere_model import SphereModel
from models.input_model import InputModel
from utils.csv_logger import log_result

def main():
    """
    Sphere CLI Calculation: get user input for a radius and precision.
    Outputs the value on the console and a running csv file.
    """
    try:
        radius = input("Enter the radius of the sphere: ")
        precision = input("Enter the decimal precision for the volume: ")
        
        input_model = InputModel()
        input_model.sphere_input(radius, precision)

        sphere = SphereModel(input_model.param1_value)
        volume = sphere.calculate()
        print(f"The volume of the sphere with radius {input_model.param1_value} is {volume:.{input_model.precision}f}")
        
        # Output to csv
        try:
            csv_output = log_result("sphere", input_model.param1_name, input_model.param1_value, volume_output=volume)
            print(f"Result added to csv file: {csv_output}")
        except TypeError as te:
            print(f"Error: {te}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
