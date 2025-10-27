#!/usr/bin/env python3
"""
WSGI entry point for the Flask application.
This file is used by gunicorn to run the application.
"""

from create_app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == "__main__":
    # For development only
    app.run(host="0.0.0.0", port=8000, debug=False)