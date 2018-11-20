"""
변수와 format 스트링을 이용해서 조금 제너럴하게 만들어보자.
"""

name = "Python"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}


def respond(user_message):
    # dictionary에 존재하는 질문인지 검사
    if user_message in responses:
        bot_message = responses[user_message]
    else:
        bot_message = responses['default']
        
    return bot_message


# 이제 반복문을 사용해보자
while True:
    user_message = input('Say Something:')
    print(respond(user_message))