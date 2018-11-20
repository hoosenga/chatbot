"""
조금 더 사용자의 질문에 유연하게 대처할 수 있도록 해보자.
"""

greeting_words = ("hello", "hi", "greetings", "sup", "what's up",)
greeting_responses = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

import random


def check_for_greeting(user_message):
    for word in user_message.split(' '):
        if word.lower() in greeting_words:
            return random.choice(greeting_responses)


while True:
    user_message = input('Say Something:')
    print(check_for_greeting(user_message))