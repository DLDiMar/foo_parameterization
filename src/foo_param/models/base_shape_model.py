class BaseModel:
    """
    BaseModel is an abstract class that defines the structure for different
    parameterization models. It provides methods to validate inputs and
    calculate the desired parameter, which should be implemented by subclasses.
    """

    def __init__(self):
        pass

    def validate_positive_number(self, value, name="value"):
        """
        Validate that a given value is a positive number.

        Args:
            value (float): The value to validate.
            name (str): The name of the value for error messaging.

        Raises:
            ValueError: If the value is not a positive number.
        """
        if value <= 0:
            raise ValueError(f"{name.capitalize()} must be a positive number.")
