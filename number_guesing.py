"""  
import random
secret_number = random.randint(1, 5)

life = 3


while life > 0:

    guess = int(input('Guess the number (1-5): '))
    
    if guess == secret_number:
        print("You got it!")
        break
    
    else:
        life -= 1
        print(f'Wrong! You have {life} attempt(s) left.')

if life == 0:
    print('Game over! You ran out of attempts.')

"""        
            
def add(a, b=[]):
    b.append(a)
    return b

print(add(1))
print(add(2))