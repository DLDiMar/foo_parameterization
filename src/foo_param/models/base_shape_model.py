class BaseModel:
    """
    Abstract class that defines the structure for different parameterization models. 
    Contains methods to validate inputs implemented by subclasses.
    """

    def __init__(self):
        pass

    def validate_positive_number(self, value, name="value"):
        """
        Validate a given value is a positive number (float or int).

        Args:
            value (float or int): The value to validate.
            name (str): The name of the value for error messaging.

        Raises:
            ValueError: If the value is not a positive number or not a float/int.
        """
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name.capitalize()} must be a number.")
        if value <= 0:
            raise ValueError(f"{name.capitalize()} must be a positive number.")
