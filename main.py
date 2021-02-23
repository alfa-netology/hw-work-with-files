import modules.own_fucntions as functions

file = 'source/recipes.txt'

# задача 1
cook_book = functions.get_cook_book(file)

dishes = ['Фахитос', 'Омлет']
person_count = 2
# задача 2
print(functions.get_shop_list_by_dishes(dishes, person_count, cook_book))

