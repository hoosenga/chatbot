"""
제어문을 사용해서 연속적으로, 여러 종류의 질문에 답변해보자.
사용자와 계속적으로 질의/응답을 진행하기 위해서 반복문(while)을 사용하자.
다양한 질문을 처리하기 위해 if 문을 사용하자.
"""

while True:
    user_message = input('Say Something...')
    user_message = user_message.lower()
    if user_message == 'bye' or user_message == 'see you':
        print('bye')
        break
    elif user_message == 'hi':
        print('hi')
    elif user_message == 'good to see you':
        print('nice to meet you')
    else:
        print("i don't get it")