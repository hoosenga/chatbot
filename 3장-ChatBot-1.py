"""
dictionary 자료형을 사용해서, 
특정 질문에 정해진 답변을 해보자
"""

# dictionary 자료형을 사용해서 질문과 응답 세트를 만들자.
responses = {
  "what's your name?": "my name is ChatBot",
  "what's today's weather?": "It's sunny.",
  "default": "any other question?"
}


def respond(user_message):
    # dictionary에 존재하는 질문인지 검사
    if user_message in responses:
        bot_message = responses[user_message]
    else:
        bot_message = responses['default']
        
    return bot_message


while True:
    user_message = input('Say Something:')
    if user_message == 'bye':
        break
    print(respond(user_message))