"""
Helper functions for the Stone-Paper-Scissors game.
"""
import os
import sys

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def ensure_directory_exists(directory):
    """Ensure that a directory exists, creating it if necessary"""
    if not os.path.exists(directory):
        os.makedirs(directory)
