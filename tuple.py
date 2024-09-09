my_city = 'Gdynia',
a_city = (53.967890, 18.533640) 
b_city = (52.229675, 21.012230) 
c_city = (53.757729, -2.703440)

for i in my_city:
    print(i)

for i in a_city:
    print(i)

for i in b_city:
    print(i)

for i in c_city:
    print(i)

all_friends_locations = a_city + b_city + c_city

print("All friends' locations combined:", all_friends_locations)