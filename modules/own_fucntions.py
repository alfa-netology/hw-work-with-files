import os

def create_dict_from_file(file_name):
    """Функция чтения файла + создание словаря нужного формата"""
    result = {}
    with open(file_name, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.lower().strip()
            counter = int(file_work.readline())
            list_of_ingredient = []
            for i in range(counter):
                ingredient_name, quantity, measure = file_work.readline().lower().strip().split(' | ')
                temp_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                }
                list_of_ingredient.append(temp_dict)
            result[dish_name] = list_of_ingredient
            file_work.readline()

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
    """
    result = []
    for file_ in files:
        with open(f'{path}{file_}', 'r', encoding='utf-8') as f:
            data = f.readlines()
            str_count = len(data)
            file_name = f.name.split('/')[1]
            item = str_count, file_name, "".join(data).strip()
            result.append(item)
    result.sort()
    result_file = 'out/result.txt'

    if os.path.isfile(result_file):
        os.remove(result_file)

    with open(result_file, 'a', encoding='utf-8') as f:
        for item in result:
            str_count, file_name, content = item
            f.write(f'{file_name}\n')
            f.write(f'{str_count}\n')
            f.write(f'{content}\n')
