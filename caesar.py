
# Define a function called caesar
def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)
    
    return encrypted_text

encrypted = caesar("Welcome to caesar encryption program", 5)
print(encrypted)