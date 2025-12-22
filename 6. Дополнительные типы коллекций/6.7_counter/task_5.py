from collections import Counter


with open('pythonzen.txt', 'r', encoding='utf-8') as f:
    text = [i for i in f.read().lower() if i.isalpha()]

for k, v in sorted(Counter(text).items(), key= lambda x: x[0]):
    print(f'{k}: {v}')