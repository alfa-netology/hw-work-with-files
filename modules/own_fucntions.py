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
                    'ingredient_name': ingredient_name.strip(),
                    'quantity': int(quantity),
                    'measure': measure,
                })
                ingredient_quantity -= 1

    if len(result) > 0:
        return result
    else:
        return False

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for item in cook_book[dish]:
                ingredient_name = item['ingredient_name']
                if ingredient_name in result:
                    quantity = item['quantity'] + result[ingredient_name]['quantity']
                else:
                    quantity = item['quantity']

                result[ingredient_name] = {
                    'measure': item['measure'],
                    'quantity': quantity,
                }
        else:
            print(f'В базе нет рецепта {dish}')

    for key in result.keys():
        result[key]['quantity'] *= person_count

    return result
