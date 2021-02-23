def get_cook_book(file_):
    """
    возвращает словарь с рецептами блюд из файла
    args:
        file_(str) : путь к файлу с рецептами
    return:
        result(dict): словарь с рецептами блюд
    """
    result = {}
    dish = ''
    ingredient_quantity = 0
    with open(file_, 'r', encoding='utf-8') as f:
        data = f.readlines()

    for line in data:
        line = line.strip()
        if line != '':
            if not line.isdigit() and '|' not in line:
                dish = line
                result[dish] = []
            elif '|' not in line:
                ingredient_quantity = int(line)

            elif '|' in line and ingredient_quantity > 0:
                ingredient_name, quantity, measure = line.split('|')
                result[dish].append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure,
                })
                ingredient_quantity -= 1
    return result