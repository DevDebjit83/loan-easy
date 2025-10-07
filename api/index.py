import sys
from pathlib import Path

# Add parent directory to path so we can import app_auth
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import the Flask app from app_auth
from app_auth import app

# Vercel will call this app directly
# No wrapper needed - just expose the Flask app
