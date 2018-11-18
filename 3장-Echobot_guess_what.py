
"""
스무 고개 게임을 만들어보자.
"""
def is_correct(guess, target):
    if guess == target:
        print("Your guess {0} is Correct!\n".format(guess))
        return True
    elif guess < target:
        print("Higher~")
        return False
    elif guess > target:
        print("Lower~")    
        return False

target = 77

def guess():
    while True:
        guess = input('Guess What between 1 to 100: ')
        if guess == '':
            break
        else:
            if is_correct(int(guess), target):
                break

if __name__ == "__main__":
    guess()
