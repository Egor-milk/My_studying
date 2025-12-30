from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap = ChainMap(*reversed(chainmap.maps))
    return chainmap.get(key, None)



