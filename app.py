
from flask import Flask, jsonify, request

import random

app = Flask(__name__)

jokes_array = [
    "Did you hear they arrested the devil? Yeah, they got him on possession.",
    "What did one DNA say to the other DNA? “Do these genes make me look fat?”",
    "My IQ test results came back. They were negative.",
    "What do you get when you cross a polar bear with a seal? A polar bear.",
    "Why can’t you trust an atom? Because they make up literally everything.",
    "Why was six afraid of seven? Because seven eight nine.",
    "What do you call a hippie’s wife? Mississippi.",
    "What’s the difference between an outlaw and an in-law? Outlaws are wanted.",
    "Scientists have recently discovered a food that greatly reduces sex drive. It’s called wedding cake.",
    "Before you marry a person, you should first make them use a computer with a slow Internet connection to see who they really are.",
    "What do kids play when their mom is using the phone? Bored games.",
    "What’s the smartest insect? A spelling bee!",
    "How does the ocean say hi? It waves!",
    "Why did the teddy bear say no to dessert? Because she was stuffed",
    "What social event do spiders love to attend? Webbings!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What’s a cat’s favorite dessert? A bowl full of mice-cream",
    "What do you call a guy who’s really loud? Mike",
    "What is a room with no walls? A mushroom",
    "Why don't eggs tell jokes? Because they might crack up!"
]


@app.route('/randomjoke', methods=['GET','POST'])
def get_random_joke():
    number = int(request.args.get('number'))
    jokes = random.choices(jokes_array,k=number)
    return (jokes)
