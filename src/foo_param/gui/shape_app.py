import tkinter as tk
from tkinter import messagebox
from foo_param.models.sphere_model import SphereModel
from foo_param.models.input_model import InputModel
from foo_param.utils.csv_logger import log_result

# Padding sizes
PADDING_SMALL = 2
PADDING_MED = 5
PADDING_LARGE = 10
WINDOW_SIZE = "300x300"

# Shape class to instantiate model calculations
class ShapeApp:
    """
    GUI application class for calculating sphere volumes.
    Initializes the main window, input models, and widgets.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Foo et al. Parameterization Tool")
        self.root.geometry(WINDOW_SIZE)

        # Initialize the input model
        self.input_model = InputModel()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and packs all the widgets in the main window.
        This includes input fields for sphere parameters and buttons for calculations.
        """
        # Sphere Section
        self.sphere_frame = tk.LabelFrame(self.root, text="Sphere Parameters", padx=PADDING_MED, pady=PADDING_MED)
        self.sphere_frame.pack(side=tk.LEFT, padx=PADDING_MED, pady=PADDING_MED, fill="both", expand=True)

        tk.Label(self.sphere_frame, text="Enter the radius of the sphere:").pack(pady=PADDING_MED, padx=PADDING_MED)
        self.radius_entry = tk.Entry(self.sphere_frame)
        self.radius_entry.pack(pady=PADDING_MED, padx=PADDING_MED)

        tk.Label(self.sphere_frame, text="Provide the decimal precision:").pack(pady=PADDING_MED, padx=PADDING_MED)
        self.precision_entry = tk.Entry(self.sphere_frame)
        self.precision_entry.pack(pady=PADDING_MED, padx=PADDING_MED)

        tk.Button(self.sphere_frame, text="Calculate Volume", command=self.calculate_sphere_volume).pack(pady=PADDING_SMALL, padx=PADDING_SMALL)

        self.volume_label = tk.Label(self.sphere_frame, text="")
        self.volume_label.pack(pady=PADDING_MED, padx=PADDING_MED)

        self.success_label = tk.Label(self.sphere_frame, text="", fg="green")
        self.success_label.pack(pady=PADDING_MED, padx=PADDING_MED)

    def calculate_sphere_volume(self):
        """
        Calculates the volume of the sphere using the provided radius and precision.
        Validates the inputs, updates the volume label, and logs the result to a CSV file.
        """
        radius_str = self.radius_entry.get()
        precision_str = self.precision_entry.get()
        if not radius_str or not precision_str:
            messagebox.showerror("Error", "Please enter both the radius and the decimal precision.")
            return

        try:
            self.input_model.sphere_input(radius_str, precision_str)
            sphere_model = SphereModel(self.input_model.param1_value)
            volume = sphere_model.calculate()
            self.volume_label.config(text=f"Volume of the sphere: {volume:.{self.input_model.precision}f}")

            # Log the result to the CSV file
            try:
                csv_output = log_result("sphere", self.input_model.param1_name, self.input_model.param1_value, volume_output=volume)
                self.success_label.config(text=f"Result added to CSV file: \n{csv_output}")
            except TypeError as te:
                self.success_label.config(text=f"Logging error: {te}", fg="red")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()
