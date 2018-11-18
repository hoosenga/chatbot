"""
파이썬의 print(), input() 함수를 이용하여 가장 기초적인 대화 시스템을 만들자.
"""

# 가장 기초적인 부분으로써 print( ) 함수로 사용자에게 질문을 유도하자.
print('Say Something...')

# 사용자로부터 질문을 받아들이자. input( ) 함수 사용
user_message = input()

# 질문에 대한 답변을 하자. 지금은 일단 EchoBack하자.
print("I can head you ! You said: " + user_message)

# 위 2가지를 아래와 같이 하나의 input( ) 함수로 처리할 수 있다.
# user_message = input('Say Something...')
# print("I can hear you! You said: " + user_message)

# 조금 다르게 하려면 아래와 같이 변수를 사용하자.
# bot_message = "I can hear you! You said: " + user_message
# print(bot_message)
