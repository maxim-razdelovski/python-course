input_string = input("please input an arbitrary number: ")

# assuming input string represents a positive integer
result = int(input_string) + int(input_string+input_string) + int(input_string+input_string+input_string)

print("result = ", result)