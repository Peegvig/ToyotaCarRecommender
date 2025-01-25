import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Test API call with the new OpenAI library format (version 1.0.0+)
try:
    # Use the new method `openai.completions.create`
    response = openai.completions.create(
        model="gpt-4",
        prompt="Recommend a good Toyota truck for off-roading.",
        max_tokens=100
    )

    print("OpenAI API Connection Successful!")
    print("AI Response:", response['choices'][0]['text'])

except Exception as e:
    print("Error connecting to OpenAI API:", e)
