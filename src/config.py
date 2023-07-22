import os
from dotenv import load_dotenv

load_dotenv()

# Define the database URIs
DATABASE_URI_WRITER = os.getenv('DATABASE_URI_WRITER')
DATABASE_URI_READER = os.getenv('DATABASE_URI_READER')
