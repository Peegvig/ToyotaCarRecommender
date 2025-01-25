from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import openai
import os

app = Flask(__name__)

# Configure MongoDB client
client = MongoClient(os.getenv("MONGO_URI"))
db = client['car_recommendations']
cars_collection = db['cars']

# Configure OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    user_data = request.json
    print("Received user data:", user_data)

    # Fetch cars from MongoDB
    cars = list(cars_collection.find({}, {"_id": 0}))

    # Prepare prompt for AI
    prompt = f"""
    Based on the following user preferences, recommend the best Toyota vehicles:
    Preferences: {user_data}
    Available cars: {cars}
    Include model name, price, and key features.
    """

    # Call OpenAI API
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "system", "content": "You are a helpful car recommendation assistant."},
    #               {"role": "user", "content": prompt}],
    #     max_tokens=500
    # )

    # recommendations = response['choices'][0]['message']['content'].strip()

    # return jsonify({"recommendations": recommendations})
    recommendations = "Here are some placeholder recommendations based on your preferences."

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
