shift = int(input("Enter a shift number to encript message: "))
message = input("Enter message: ")

shfited_message = message[shift:] + message[0:shift]
print(shfited_message.strip())

