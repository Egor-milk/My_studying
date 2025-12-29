from collections import ChainMap


def deep_update(chainmap : ChainMap, key, value):
    if key in chainmap:
        for i in chainmap.maps:
            if key in i:
                i[key] = value
    else:
        chainmap.maps[0][key] = value

chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')
print(chainmap)
