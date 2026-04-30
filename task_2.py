

def get_cats_info(path):
    with open(path, "r", encoding='utf-8') as fh:
        lines = [el.strip() for el in fh.readlines()]
        list_of_cats = []
        for line in lines:
            data = line.split(',')
            id, name, age = data
            d = {'id': id, 'name' : name, 'age': age}
            list_of_cats.append(d)
    
    return list_of_cats

try:
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
except FileNotFoundError:
    print("No file available.")