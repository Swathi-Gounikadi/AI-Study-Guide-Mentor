import os
from dotenv import load_dotenv
from langfuse import Langfuse


# Load environment variables
load_dotenv()

# Initialize Langfuse client
langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_BASE_URL","https://us.cloud.langfuse.com")
)

print("✅ Langfuse initialized successfully!")