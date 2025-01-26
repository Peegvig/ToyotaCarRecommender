from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from openai import OpenAI
from pymongo import MongoClient
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    user_data = request.json

    # Prepare prompt for AI
    prompt = f"""
    Based on the following user preferences, recommend the 3 best Toyota vehicles:
    Preferences: {user_data}
    Include model name, price, and key features.
    Do not under any circumstances recommend a vehicle that does not fall in the users price range.
    Do not say anything else other than the bulleted list with 3 vehicles each with 3 key features in a nested list.
    If the minimum price of the vehicle is above the maximum price do not list the vehicle, under this circumstance it is ok to list less than 3 cars.
    NEVER EVER RECOMMEND A CAR ABOVE THE PRICE RANGE!
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        recommendations = response.text if response else "No recommendations available."

        return jsonify({"recommendations": recommendations})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
