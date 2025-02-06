from functools import reduce


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), 
            ('Just Like That', 5.05), 
            ('Song 3', 6.8), 
            ('Leave The Door Open', 4.02), 
            ('I Can\'t Breath', 4.47), 
            ('Bad Guy', 3.14)
            ]

def filter_more_than_five(song):
    return song[1] > 5.00

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100
    total_seconds = minutes * 60 + round(seconds)
    return total_seconds

def add_durations(total, song):
    duration = song[1]
    return total + duration


songs_longer_than_five_minutes = list(filter(filter_more_than_five, playlist))

convert_minutes_to_seconds = list(map(minutes_to_seconds, playlist))

total_playtime = reduce(add_durations, playlist, 0)

print(songs_longer_than_five_minutes)  # Lista piosenek >5 min
print(convert_minutes_to_seconds)      # Czasy w sekundach
print(total_playtime) 



