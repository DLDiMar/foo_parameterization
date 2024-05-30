class InputModel:
    """
    InputModel handles user inputs for the sphere parameters.
    """

    def __init__(self):
        self.precision = None
        self.param1_name = ""
        self.param1_value = ""
        self.param2_name = ""
        self.param2_value = ""
        self.param3_name = ""
        self.param3_value = ""

    def sphere_input(self, radius, precision):
        """
        Set user input for the sphere parameters.
        """
        try:
            self.param1_name = "radius"
            self.param1_value = float(radius)
            self.precision = int(precision)
        except ValueError as e:
            raise ValueError(f"Error: {e}")
