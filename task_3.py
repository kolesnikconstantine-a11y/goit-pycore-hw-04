
import sys
from pathlib import Path
from colorama import Fore, Style

# Перевірка, чи передан скрипту абсолютний шлях до директоріЇ як параметр
if len(sys.argv) < 2:
    print('Please provide path')
    sys.exit()

# шлях до директорії як аргумент при запуску. Цей шлях вказує,
#  де знаходиться директорія, структуру якої потрібно відобразити.
file_path = Path(sys.argv[1])

def parse_folder(mypath):
    for el in mypath.iterdir():
        if el.is_dir():
            print(Fore.BLUE + f"    {el.name}")
            parse_folder(el)
        else:
            print(Fore.GREEN +f"    {el.name}")
    print(Style.RESET_ALL)

# Перевірка, чи файл існує, перш ніж виконунувати функцію
if file_path.is_dir():
    print(Fore.BLUE + f'{file_path}')
    parse_folder(file_path)
else:
    print(f'Шлях {file_path} не існує')
    sys.exit()

