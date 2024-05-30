import tkinter as tk
from gui.shape_app import ShapeApp

def main():
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
