from pathlib import Path


# Функція повинна точно обчислювати загальну та середню суми.
# приймати один аргумент - шлях до текстового файлу (path).
def total_salary(path):
    # Відкриття текстового файлу з явним вказівкам UTF-8 кодування
    with open(path, "r", encoding='utf-8') as fh:
        lines = [el.strip() for el in fh.readlines()]
        #content = fh.read()
        total = 0
        for line in lines:
            data = line.split(',')
            total += int(data[1])
            avarage = total / len(lines)
    # Результатом роботи функції є кортеж із двох чисел: 
    # загальної суми зарплат і середньої заробітної плати.
    return total, avarage
   
try:
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
#Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
except FileNotFoundError:
    print("No file available.")
