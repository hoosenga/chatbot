# 특정한 일만 하는 함수
'''
함수는 반복되는 작업에 의한 불필요한 작업을 줄이고, 
프로그램의 재 사용성을 높일 수 있도록 해주며, 
또한 긴 프로그램을 작성할 때, 연관된 부분끼리 함수라는 단위로 묶음으로써 
긴 소스 코드들을 효율적으로 관리할 수 있다.
함수의 기능은 음악 악보에서 ‘후렴’이라고 생각하면 된다. 
예를 들어, 애국가 1절을 부르고, (후렴)을 부르고, 
또 2절을 부르고 (후렴)을 부르는 경우, 
매번 후렴을 반복해서 악보에 쓰기 귀찮으니까, 
후렴이라고 뭉쳐놓고, (후렴) 부르세요… 라고 말만하면 되는 것처럼, 
함수의 기본적인 역할은 반복되는 부분의 재 사용성을 높이는 역할이다.
'''
def greet1():
    print('Hi')

greet1()

# 값을 반환하는 함수
def greet2():
    return 'Hello'

print(greet2())

# 값을 전달받는 함수
'''
수학에서 사용하는 삼각 함수 중에서 사인 함수는 sin(30)과 같이 괄호에 숫자로 값을 전달한다. 
그러면 sin( ) 함수는 전달받은 값에 해당하는 sin 값을 반환한다.
C 언어에서도 함수에 값을 전달하고 싶은 경우가 있다. 
우리가 사용한 print(“Hello, World”) 함수 호출은 
printf( ) 함수에게 문자열을 넘겨준 것이다. 
이렇게 함수에 전달하는 값을 매개 변수(parameter, 파라미터)라고 한다. 
아래와 같이 함수에 매개 변수를 사용할 경우에는, 
함수를 “정의”할 때 매개 변수의 개수, 종류, 이름 등을 정해야한다. 
매개 변수: 파라미터(parameter)라고도 한다. 
함수를 사용할 때 괄호 속에 적어서 넘겨주는 값을 말한다. 
매개 변수라는 용어는 호출하는 함수(caller)와 호출되는 함수(callee) 사이에 
데이터를 연결(매개)해준다는 의미.

'''
def greet3(message):
    print(message)

print('Say Hi!')


# 값을 전달받고, 또, 반환하는 함수
'''
파라미터도 전달하고, 반환값도 있다.
'''
def sum(a, b):
    return a+b

c = sum(1, 2)
print(c)

a = 2
b = 4
c = sum(a, b)
print(c)

# 반환값이 없는 함수의 반환값은 무엇일까?
'''
함수의 끝에 명시적인 return 문장이 없거나,
return 문장만 있고, 실제로 반환하는 값이 없는 경우에는
자동으로 None 값을 반환한다.
즉, 파이썬의 모든 함수는 값을 반환하도록 되어있다.
'''
def greet4():
    print('Hi')
    return

print(greet1())
print(greet4())

# 아래의 코드를 보자.
# 이 문장은 TEST를 출력한 후, # NONE을 출력한다. 
# 즉, PRINT( ) 함수는 NONE이라는 값을 반환한다는 의미다.
# 이 내용은 함수 부분에서 자세하게 다시 설명한다.
print(print('test')


# 2개 이상의 값을 반환하고 싶을 때는
def arithmetic_operation(a, b):
    return a+b, a-b, a*b, a/b

c = arithmetic_operation(1, 2)
print(type(c))
print(c)

a, b, c, d = arithmetic_operation(1,2)
print(a, b, c, d)


# 위치 인자(positional parameter)와 키워드 인자(keyword parameter)
def print_message(a, b, c):
    print(a, b, c)

print_message(1, 2, 3)
print_message(a=1, b=2, c=3)
print_message(c=1, b=2, a=3)
print_message(1, b=2, c=3)
# print_message(1, b=2, 3)


# 파라미터의 디폴트 값 설정
def greet4(message='Nice to meet you'):
    print(message)

greet4('hi')
greet4()

# 디폴트 파라미터 값 설정 시 주의
def greet5(name, day, year='2018'):
    print('Hi '+name+'. Today is '+ day + '. ' + year)

greet5('Ben', 'Monday', '2018')
greet5('Ben', 'Monday')

# 아래와 같이 디폴트 값을 설정한 파라미터 이후에는 디폴트값을 설정하지 않는 파라미터를 사용할 수 없다.
'''
def greet6(name, year='2018', day):
    print('Hi '+name+'. Today is '+ day + '. ' + year)

greet5('Ben', 'Monday', '2018')
greet5('Ben', 'Monday')
'''

# 함수 내부의 지역 변수의 범위
a = 10
def test1(a):
    a = a + 1

test1(a)
print(a)


a = 10
def test2(a):
    a = a + 1
    return a

a = test2(a)
print(a)


a = 10
def test3():
    global a  # 가급적 global 명령어는 사용하지 말자
    a = a + 1

test3()
print(a)