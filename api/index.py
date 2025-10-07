import sys
import os

# Add parent directory to path to import app_auth
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app_auth import app

# Export for Vercel - this is what Vercel will call
# No need to rename, just ensure it's imported
