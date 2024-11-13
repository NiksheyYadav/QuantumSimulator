from setuptools import setup, find_packages

# Project information
project_name = "Quantum Simulator"  # Replace with your project name
version = "0.0.1"  # Replace with your project version
description = "Simulate quantum systems"  # Replace with a short description
author = "Nikshey Yadav"  # Replace with your name
author_email = "relativity1905e@gmail.com"  # Replace with your email

# Dependencies (if any)
requirements = [
    "numpy",  # Replace with any required libraries
    "scipy",  # You can add more dependencies here
]

setup(
    name=project_name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(where="quantum_simulation"),  # Finds packages automatically
    install_requires=requirements,  # Installs listed dependencies
)