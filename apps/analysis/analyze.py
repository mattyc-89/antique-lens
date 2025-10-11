from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

from .prompts import system_prompt

def analyze_image(image_path):
    load_dotenv() # Load environment variables from .env file
    client = genai.Client() # Initialize the GenAI client, retrieve API key from environment variable 
    
    img = Image.open(image_path)  # Open and preprocess the image

    user_prompt = "" 

    # Create the initial message list with the user prompt and image
    messages = [
        types.content(
            role="user", 
            parts=[
                types.Part(text=user_prompt),
                types.Part(image=types.Image(img))
            ]
        )
    ]
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            ),
        )
        
        import json
        analyze_results = json.loads(response.text)
        return analyze_results
    
    except Exception as e:
        print(f"An error occurred during image analysis: {e}")
        return None

    

