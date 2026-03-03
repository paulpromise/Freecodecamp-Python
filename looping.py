""" 
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)
    
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

secret_number = 3
guess = 0
life = 3

while (guess != secret_number):
    guess =  int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')
print('You got it!')
"""

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
        
languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1
    
print(list(enumerate(languages)))
for index, language in enumerate(languages):
    print(f"Index {index} and language {language}")