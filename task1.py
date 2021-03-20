color, lucky_number = 'red', 7

print(color, end='!\n')
print(lucky_number)

# printing in a slightly different way
print(color, lucky_number, sep='!\n')

color = input("input your favorite color: ")

lucky_number = int(input("input your lucky number: "))

print(f"your color is: '{color}' and your number is '{lucky_number}'")

