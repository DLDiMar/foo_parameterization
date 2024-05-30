import pytest
import numpy as np
from foo_param.models.sphere_model import SphereModel

def test_sphere_model_initialization():
    radius = 5
    sphere_model = SphereModel(radius)
    assert sphere_model.radius == radius

def test_sphere_model_validate_positive_radius():
    radius = 5
    sphere_model = SphereModel(radius)
    sphere_model.validate()  # Should not raise an exception

def test_sphere_model_validate_zero_radius():
    radius = 0
    sphere_model = SphereModel(radius)
    with pytest.raises(ValueError, match="Radius must be a positive number"):
        sphere_model.validate()

def test_sphere_model_validate_negative_radius():
    radius = -5
    sphere_model = SphereModel(radius)
    with pytest.raises(ValueError, match="Radius must be a positive number"):
        sphere_model.validate()

def test_sphere_model_calculate_volume():
    radius = 3
    sphere_model = SphereModel(radius)
    expected_volume = (4/3) * np.pi * radius**3
    volume = sphere_model.calculate()
    assert volume == pytest.approx(expected_volume, 0.001)

def test_sphere_model_calculate_volume_invalid_radius():
    radius = -3
    sphere_model = SphereModel(radius)
    with pytest.raises(ValueError, match="Radius must be a positive number"):
        sphere_model.calculate()

# Run the tests
if __name__ == "__main__":
    pytest.main()
