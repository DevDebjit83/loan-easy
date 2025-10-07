"""
WSGI entry point for Vercel deployment
"""
from app_auth import app

# Vercel expects the Flask app to be named 'app' or exported as a function
if __name__ == "__main__":
    app.run()
