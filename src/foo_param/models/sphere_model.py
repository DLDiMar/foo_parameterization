from .base_shape_model import BaseModel
import numpy as np

class SphereModel(BaseModel):
    """
    SphereModel calculates the volume of a sphere given its radius.
    """

    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        """
        Validate the radius. The radius must be a positive number.

        Raises:
            ValueError: If the radius is not positive.
        """
        self.validate_positive_number(self.radius, "radius")

    def calculate(self):
        """
        Calculate the volume of the sphere after validating the radius.

        Returns:
            float: The volume of the sphere.
        """
        self.validate()
        return (4/3) * np.pi * self.radius**3
