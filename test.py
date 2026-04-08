from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API =os.getenv("GOOGLE_API_KEY")
print(GOOGLE_API)

