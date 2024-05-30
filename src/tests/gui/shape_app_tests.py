import pytest
from foo_param.models.sphere_model import SphereModel
from foo_param.models.input_model import InputModel
from foo_param.utils.csv_logger import log_result
import os
from datetime import datetime
import getpass

# Test InputModel
def test_input_model():
    input_model = InputModel()
    input_model.sphere_input("3", "2")
    assert input_model.param1_value == 3
    assert input_model.precision == 2

    with pytest.raises(ValueError):
        input_model.sphere_input("invalid", "2")

    with pytest.raises(ValueError):
        input_model.sphere_input("3", "invalid")

# Test SphereModel
def test_sphere_model():
    sphere_model = SphereModel(3)
    volume = sphere_model.calculate()
    assert volume == pytest.approx(113.097, 0.001)

    with pytest.raises(ValueError):
        sphere_model = SphereModel(0)
        sphere_model.calculate()

# Test log_result
def test_log_result(tmpdir): 
    result = log_result("sphere", "radius", 3, volume_output=113.097)

    # Ensure the file was created in the expected location
    assert os.path.isfile(result)
    
    # Open the created file and verify its contents
    with open(result, "r") as f:
        lines = f.readlines()
        assert len(lines) >= 2  # Assuming there's a header line and at least one data line
        
        header = lines[0].strip().split(',')
        expected_header = ['date', 'username', 'shape', 'param1_name', 'param1_value', 'param2_name', 'param2_value', 'param3_name', 'param3_value', 'volume_output']
        assert header == expected_header
        
        data = lines[1].strip().split(',')
        assert data[2] == "sphere"
        assert data[3] == "radius"
        assert data[4] == "3"
        assert data[9] == "113.097"

# Run the tests
if __name__ == "__main__":
    pytest.main()
