# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Final Project


# Proper import of packages used.
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app

