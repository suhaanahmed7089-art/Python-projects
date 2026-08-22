# Personal chat assisstant that responses to basic questions

import random
import datetime
import time
present_hour=datetime.datetime.now().hour
# Taking userinput for their name
name=input("Enter your name: ")

if present_hour>=5 and present_hour<12:
    print(f"Good Morning, {name}. How can I help you")
elif present_hour>=12 and present_hour<17:
    print(f"Good Afternoon, {name}. How can I help you")
elif present_hour>=17 and present_hour<21:
    print(f"Good evening, {name}. How can I help you")
else:
    print(f"Good night, {name}. How can I help you")

# Creating dictionary for assistant responses

responses = {
    "hello":"Hello, how can i help you",
    "how are you":"I am fine what about you. How was your day",
    "tell me a joke":"Waiter: Would you like coffee or tea? Programmer: Yes.",
    "motivate me": "You have infinite chances as long as you are alive",
    "who are you":"Don't hurt my feelings, Don't you know me. Just kidding, i am your personal chat assisstant",
    "thanks": "You're very welcome!",
}

def get_response(user_question):
    user_question=user_question.lower()
    for eachkey in responses:
        if eachkey in user_question:
            return responses[eachkey]

    fallback=[
        "Sorry, I am not able to answer your question",
        "that's interesting, could you tell me more about it",
        "I am still learning. What do you mean by that",
        "I see, that's a good point",
        "Can we skip this....",
        "that's a very hard question"
    ]
    return random.choice(fallback)

while True:
    # Take user input to ask a question
    user_input=input("Ask a Question: ")
    reply=get_response(user_input)
    print(f"Bot response: {reply}")

    if "bye" in user_input.lower():
        print("Goodbye!!")
        break
