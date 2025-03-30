import os
from dotenv import load_dotenv

load_dotenv()

PRAW_SECRET = os.environ.get("PRAW_SECRET", None)
PRAW_USER_CLIENT = os.environ.get("PRAW_USER_CLIENT", None)
PRAW_KEY = os.environ.get("PRAW_KEY", None)

