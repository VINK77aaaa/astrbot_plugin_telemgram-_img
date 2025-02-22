import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration settings
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "default_session")
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 5))
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "downloads")