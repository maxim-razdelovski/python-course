"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

file_obj = open("task2-text.txt", "r")

count_lines = 0
count_words = 0

for line in file_obj:
    count_lines += 1
    count_words += len(line.split())

print(f"file '{file_obj.name}' has total {count_lines} lines and {count_words} words")