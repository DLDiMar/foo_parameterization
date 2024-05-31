import tkinter as tk
from .shape_app import ShapeApp

def gui_main():
    root = tk.Tk()
    app = ShapeApp(root)
    root.mainloop()

if __name__ == "__main__":
    gui_main()