import os

def get_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")
    return api_key

def set_api_key(api_key):
    if not api_key:
        raise ValueError("Invalid API key provided.")
    os.environ['OPENAI_API_KEY'] = api_key