from models.sphere_model import SphereModel
from models.input_model import InputModel
from utils.csv_logger import log_result

def main():
    """
    Sphere CLI Calculation: get user input for a radius and precision.
    Outputs the value on the console and a running csv file.
    """
    try:
        input_model = InputModel()
        input_model.sphere_input()

        input_model.param1_name = "radius"
        sphere = SphereModel(input_model.param1_value)
        volume = sphere.calculate()
        print(f"The volume of the sphere with radius {input_model.param1_value} is {volume:.{input_model.precision}f}")
        # Output to csv
        log_result("sphere", input_model.param1_name, input_model.param1_value, volume_output=volume)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
