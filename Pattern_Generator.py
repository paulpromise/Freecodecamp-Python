def number_pattern(n):
    if not isinstance(n, int):
        
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."
    

    
    return " ".join(str(num) for num in range(1, n + 1))
        


        
#print(number_pattern(42))


programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(programming_languages.index('Python', 3))