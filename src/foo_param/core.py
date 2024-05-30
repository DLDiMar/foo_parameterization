from models.sphere_model import SphereModel

def main():
    try:
        radius = float(input("Enter the radius of the sphere: "))
        precision = int(input("Enter the decimal precision for the volume: "))

        sphere = SphereModel(radius)
        volume = sphere.calculate()
        print(f"The volume of the sphere with radius {radius} is {volume:.{precision}f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
