import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

# Mapped names
def capitalize_suffix(name):
  return name.capitalize()

capp_suffixes = list(map(capitalize_suffix,suffixes))

# List comprehensions
random_names = [create_fantasy_name(prefixes, capp_suffixes) for name in range(10)]


# Filtered names
def fire_in_username(name):
    return 'Fire' in name
filtered_names = list(filter(fire_in_username, random_names))

# Reduced list based on filtered names
def concatenate_names(acc, name):
    return acc + ',' + name

reduced_names =reduce(concatenate_names, filtered_names)


def display_name_info():
    print('Fantasy Names:')
    for name in random_names:
        print(name)
    print()
    print('Filtered names with \'Fire\':', filtered_names)
    print('Concatenated names:', reduced_names) 

display_name_info()






  