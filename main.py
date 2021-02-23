import modules.own_fucntions as functions

# задача 1
file = 'source/recipes.txt'
cook_book = functions.create_dict_from_file(file)

# задача 2
dishes = ('фахитос', 'омлет', 'хинкали')
person_count = 2
print(functions.get_shop_list_by_dishes(dishes, person_count, cook_book))

# задача 3
path = 'source/'
files = ['1.txt', '2.txt', '3.txt']
functions.sort_source_files(path, files)








