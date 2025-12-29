from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

price_list = ChainMap(bread, meat, sauce, vegetables, toppings)
summary = 0
max_len = max(len(k) for k in price_list)
a = input()
compound = Counter(a.split(','))
for k, v in sorted(compound.items(), key=lambda item: item[0]):
    price = price_list[k] * v
    print(f'{k.ljust(max_len)} x {v}')
    summary += price
print('-' * (max_len + 3 + len(str(max(compound.values())))))
print(f'ИТОГ: {summary}')