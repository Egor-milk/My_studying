from collections import ChainMap


def get_all_values(chainmap : ChainMap, key):
    temp_obj = chainmap.maps
    answer = set()
    for i in temp_obj:
        if key in i:
            answer.add(i[key])
    return answer

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')
print(result)