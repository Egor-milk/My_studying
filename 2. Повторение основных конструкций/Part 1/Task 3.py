def is_valid(our_string):
    if len(our_string) in range(4, 7) and our_string.isdigit():
        return True
    else:
        return False

print(is_valid('49 83'))    
