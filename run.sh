#!/bin/bash

# Update packages and install Python
sudo apt-get update
sudo apt-get install python3

# Install Flask
pip3 install flask

# Install CSV handling library
pip3 install csv

# Initialize project (assuming there's a command for this)
# Replace 'init_project' with the actual command to initialize the project
init_project

# Run the Flask application
python3 app.py