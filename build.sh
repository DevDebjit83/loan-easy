#!/bin/bash

# Exit on error
set -o errexit

echo "--- Installing Python dependencies ---"
pip install -r requirements.txt

echo "--- Initializing the database ---"
# This command will find the Flask app in wsgi.py and run the init_app function
# which contains db.create_all()
flask --app app_auth init_app

echo "--- Build complete ---"
