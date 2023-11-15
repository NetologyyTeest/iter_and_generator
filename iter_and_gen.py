# Итератор
class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.list_of_lists = [item for sublist in self.list_of_lists for item in sublist]
        return self

    def __next__(self):
        if self.list_of_lists:
            return self.list_of_lists.pop(0)
        else:
            raise StopIteration


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)






# Генератор
def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]
for item in  flat_generator(nested_list_1):
	print(item)
flat_list_1 = [item for item in flat_generator(nested_list_1)]
print(flat_list_1)