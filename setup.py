from setuptools import setup, find_packages

setup(
    name="foo_et_al_param",
    version="0.1.0",
    description="A package for Foo et al. parameterization calculations",
    author="Dominic DiMarco",
    author_email="dominic.l.dimarco@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "foo_et_al_param=foo_param.core:core_main",
        ],
        "gui_scripts": [
            "foo_et_al_param_gui=foo_param.gui:gui_main",
        ],
    }
)
