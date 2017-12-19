def read_cook_book():
    cook_book = {}
    with open('Dishes') as f:
        while True:
            dish_name = f.readline()
            dish_name = dish_name.strip()

            if not dish_name:
                break

            cook_book[dish_name] = []
            counter = int(f.readline())

            for i in range(counter):
                tmp = f.readline()
                tmp = tmp.strip()
                tmp_list = tmp.split(' | ')
                tmp_list[1] = int(tmp_list[1])
                tmp_dict = {'ingridient_name': tmp_list[0], 'quantity': tmp_list[1], 'measure': tmp_list[2]}
                cook_book[dish_name].append(tmp_dict)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)


cook_book = read_cook_book()
create_shop_list(cook_book)
