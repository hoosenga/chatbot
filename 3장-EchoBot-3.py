"""
이제 함수를 사용해보자. 
챗봇의 응답을 생성하는 함수를 만들것이다.
"""

# 함수를 사용해보자. 아래는 respond( )라는 함수를 정의하고 있다.
def respond(user_message):
    if user_message == 'bye' or user_message == 'see you':
        return('bye')
    elif user_message == 'hi':
        return('hi')
    elif user_message == 'good to see you':
        return('nice to meet you')
    else:
        return("i don't get it")


while True:
    user_message = input('Say Something...')
    if user_message == '':
        break
    else:
        user_message = user_message.lower()
        chatbot_message = respond(user_message)
        print(chatbot_message)
    
    