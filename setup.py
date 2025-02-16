from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


# Probably should be changed, __init__.py is no longer required for Python 3
for dirpath, dirnames, filenames in os.walk("carculator_bus"):
    # Ignore dirnames that start with '.'
    if "__init__.py" in filenames:
        pkg = dirpath.replace(os.path.sep, ".")
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, ".")
        packages.append(pkg)


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


setup(
    name="carculator_bus",
    version="0.0.3",
    packages=packages,
    author="Romain Sacchi <romain.sacchi@psi.ch>",
    license=open("LICENSE").read(),
    package_data={"carculator_bus": package_files(os.path.join("carculator_bus", "data"))},
    install_requires=[
        "pandas",
        "xarray",
        "numpy",
        "pytest",
        "pytest-cov",
        "klausen",
        "xlrd",
        "pytest",
        "numexpr",
        "bw2io",
        "prettytable",
        "wurst",
        "pycountry"
    ],
    url="https://github.com/romainsacchi/carculator_bus",
    description="Prospective environmental and economic life cycle assessment of urban and coach buses",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
)
