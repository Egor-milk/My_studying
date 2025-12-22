from collections import Counter

for k, v in sorted(Counter(input().split(',')).items(), key= lambda x: x[0]):
    price = sum([ord(i) for i in k])
    print(f'{k}: {price} UC * {v} = {price * v} UC')