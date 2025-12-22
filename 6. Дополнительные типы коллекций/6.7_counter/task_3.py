from collections import Counter

for k, v in sorted(Counter(input().split(',')).items(), key= lambda x: x[0]):
    print(f'{k}: {v}')