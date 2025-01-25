from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

try:
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": "Recommend a good Toyota truck for off-roading.",
        }],
        model="gpt-3.5-turbo",
    )
    print("AI Response:", chat_completion.choices[0].message.content)

except Exception as e:
    print("Error connecting to OpenAI API:", e)
