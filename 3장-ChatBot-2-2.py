# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 11:30:40 2018

@author: jungkeechul
"""

"""
dictionary 자료형을 사용해서, 
특정 질문에 정해진 답변을 해보자
"""

# dictionary 자료형을 사용해서 질문과 응답 세트를 만들자.
responses = {
  ("hello", "hi", "greetings", "sup", "what's up",): "hi~",
  ("name", "name please", "your name", "what's your name?"): "my name is ChatBot",
  ("weather", "hows weather", "what's today's weather?"): "It's sunny."
  }


def respond(user_message):
    # dictionary에 존재하는 모든 key(tuple)에 대해서
    for user_messages in responses:
        # 해당하는 tuple에 질문이 포함되는지
        if user_message in user_messages:
            return responses[user_messages]


while True:
    user_message = input('Say Something:')
    if user_message == 'bye':
        print("See you soon ~")
        break
    print(respond(user_message))