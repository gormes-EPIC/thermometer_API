#!/bin/bash

# Set variables
REPO_DIR="/home/pi/therm_api/thermometer_API"
PYTHON_FILE="therm_api.py"  

# Go to repo
cd "$REPO_DIR" || exit

# Pull latest changes
git pull origin main 

# Run the Python file
python3 "$PYTHON_FILE"
