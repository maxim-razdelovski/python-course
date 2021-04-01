input_number = int(input("input positive integer number, please: "))

decimated_number = input_number // 10
max = input_number % 10

while decimated_number > 0:
    if decimated_number % 10 > max:
        max = decimated_number % 10

    decimated_number = decimated_number // 10


print("biggest number is: ", max)