#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up the database..."
python3 setup.py

echo "Setup complete! You can now run the app."

