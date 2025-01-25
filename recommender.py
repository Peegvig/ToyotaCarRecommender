from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from pymongo import MongoClient
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure MongoDB client
# client = MongoClient(os.getenv("MONGO_URI"))
# db = client['car_recommendations']
# cars_collection = db['cars']
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    user_data = request.json
    print("Received user data:", user_data)

    # Fetch cars from MongoDB
    # cars = list(cars_collection.find({}, {"_id": 0}))

    # Prepare prompt for AI
    print(user_data)
    prompt = f"""
    Based on the following user preferences, recommend the 3 best Toyota vehicles:
    Preferences: {user_data}
    Include model name, price, and key features.
    Do not under any circumstances recommend a vehicle that does not fall in the users price range.
    Do not say anything else other than the bulleted list with 3 vehicles each with 3 key features in a nested list.
    If the minimum price of the vehicle is above the maximum price do not list the vehicle, under this circumstance it is ok to list less than 3 cars.
    NEVER EVER RECOMMEND A CAR ABOVE THE PRICE RANGE!
    """

    # Call OpenAI API
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="gpt-3.5-turbo",
    )
    print("AI Response:", chat_completion.choices[0].message.content)
    return jsonify({"recommendations": chat_completion.choices[0].message.content})


if __name__ == '__main__':
    app.run(debug=True)
