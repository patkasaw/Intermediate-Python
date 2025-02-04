# Task 1: Create Player Data
players_data = [
    {'name': 'Patrick Mahomes', 'position': 'Quarterback', 'jersey_number': 12, 'yards_gained': 140, 'touchdowns': 0},
    {'name': 'Tyreek Hill', 'position': 'Wide Receiver', 'jersey_number': 10, 'yards_gained': 150, 'touchdowns': 2},
    {'name': 'Travis Kelce', 'position': 'Tight End', 'jersey_number': 13, 'yards_gained': 170, 'touchdowns': 3},
]
# Print out a list of all player positions in the dataset.

names = [player['name']for player in players_data]
print('Players names:', names)

positions = [player['position']for player in players_data]
print('Players position:', positions)

jersey_numbers = [player['jersey_number']for player in players_data]
print('Players jersey number:', jersey_numbers)

yards_gained = [player['yards_gained']for player in players_data]
print('Players yards gained:', yards_gained)

touchdowns = [player['touchdowns']for player in players_data]

#Choose a player and update their game statistics in the dataset.

players_data[2]['yards_gained'] += 30

players_data[0]["touchdowns"] += 1

print(players_data)

#Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.

yards_gained_average = sum(player['yards_gained'] for player in players_data) / len(players_data)

touchdowns_average = sum(player['touchdowns'] for player in players_data) /len(players_data)

print('Average yards gained:', yards_gained_average)

print('Average touchdowns:', touchdowns_average)
