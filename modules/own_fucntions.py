import os

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
    """
    получает список покупок ингредиентов
    для блюд из книги рецептов
    для определенного количества человек\n
    args:\n
    dishes(tuple): список блюд\n
    person_count(int): количество персон\n
    cook_book(dict): книга рецептов
    """
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

def sort_source_files(path, files):
    """
    возвращает файл собраный по условию задачи.
    что бы отсротировать файлы по количеству строк,
    добавляю в список списков данные и содержание файла
    [[количество строк#имя файла#содержание], [...]]
    замем result.sort()
    после при выводе разбиваю строку по #
    и записываю в переменные file_name, str_count, content
    решение не самое элегантное, но уж какое родилось))
    """
    result = []
    for file_ in files:
        with open(f'{path}{file_}', 'r', encoding='utf-8') as f:
            data = f.readlines()
            str_count = len(data)
            file_name = f.name.split('/')[1]
            item = f'{str_count}#{file_name}#{"".join(data).strip()}'
            result.append(item)
    result.sort()

    result_file = 'out/result.txt'

    if os.path.isfile(result_file):
        os.remove(result_file)

    with open(result_file, 'a', encoding='utf-8') as f:
        for item in result:
            str_count, file_name, content = item.split('#')
            f.write(f'{file_name}\n')
            f.write(f'{str_count}\n')
            f.write(f'{content}\n')
