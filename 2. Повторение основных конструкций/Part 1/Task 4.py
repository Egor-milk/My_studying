def print_given(*args, **kwargs):
    for i in args:
        print(f'{i} {type(i)}')
    for key, value in sorted(kwargs.items()):
        print(f'{key} {value} {type(value)}')

print(print_given())
