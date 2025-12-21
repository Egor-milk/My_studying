from collections import OrderedDict



def custom_sort(ordered_dict: OrderedDict, by_values=False):
    deep_copy = list(ordered_dict.items())
    deep_copy.sort(key=lambda x: x[by_values])
    for k, v in deep_copy:
        ordered_dict.move_to_end(k)



data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())