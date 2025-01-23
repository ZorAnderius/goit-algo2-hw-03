import csv
from BTrees.OOBTree import OOBTree
import timeit

def load_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def add_item_to_tree(tree: OOBTree, item: dict) -> None:
    tree[int(item['ID'])] = item

def add_item_to_dict(dict: dict, item: dict) -> None:
    dict[int(item['ID'])] = item

def range_query_tree(tree: OOBTree, min_price: int, max_price: int) -> list:
    results = []
    for key, value in tree.items(min_price, max_price):
        price_as_float = float(value['Price'])
        if min_price <=price_as_float <= max_price:
            results.append(value)
    return results

def range_query_dict(dict: dict, min_price: int, max_price: int) -> list:
    results = []
    for key, value in dict.items():
        price_as_float = float(value['Price'])
        if min_price <= price_as_float <= max_price:
            results.append(value)
    return results

def task2() -> None:
    data = load_data("generated_items_data.csv")

    oobtree = OOBTree()
    dictionary = {}

    for item in data:
        add_item_to_tree(oobtree, item)
        add_item_to_dict(dictionary, item)

    min_price = 100
    max_price = 500

    time_oobtree = timeit.timeit(lambda: range_query_tree(oobtree, min_price, max_price), number=100)
    print("Total range_query time for OOBTree:", time_oobtree, "seconds")

    time_dict = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)
    print("Total range_query time for Dict:", time_dict, "seconds")

if __name__ == '__main__':
    task2()