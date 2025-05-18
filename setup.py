# What Does "Local Package" Mean?
# A local package is:

# A folder you created (not downloaded from internet).

# Structured like a Python library.

# Installed only on your computer or virtual environment.

# Used to keep your project organized and importable.
# We create a local package so that our project can be installed and reused just like any other Python library — but it's made by us, and used only on our computer or project.



from setuptools import find_packages, setup

setup(
    name='Generative AI Project',
    version='0.0.0',
    author='Arjun',
    author_email='arjunarjunkp51@gmail.com',
    packages=find_packages(where='src'),    # <-- look inside src folder
    package_dir={"": "src"},                 # <-- tell setuptools that root package is in src
    install_requires=[],                     # empty list, or add dependencies here
)
