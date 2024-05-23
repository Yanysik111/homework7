my_dict = {'Sveta': 1999, 'Katya': 2001, 'Ivan': 1998, 'Sergey': 2000, 'Anna': 1997}
print(my_dict)
print(my_dict['Sveta'])
print(my_dict.get('Dasha','Not Found'))
my_dict['Stas'] = 1995
my_dict['Tanya'] = 1998
print(my_dict.pop('Ivan'))
print(my_dict)
my_set = {4, 6, 15, '77', 15, '23', 6}
print(my_set)
my_set.update([66, 38])
my_set.discard(6)
print(my_set)