import os
from dotenv import load_dotenv

load_dotenv()

DB_ROOT_PATH = os.getenv('DB_ROOT_PATH')
PROJECT_ROOT_PATH = os.getenv('PROJECT_ROOT_PATH')
