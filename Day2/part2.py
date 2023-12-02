file = open('part1.txt', 'r')
lines = file.readlines()
cubes = {'red': 0, 'green':0, 'blue':0}

def strip_game_numbers(game_list):
   stripped_list = []
   for game in game_list:
       stripped_game = game.split(': ')[1]
       stripped_game = stripped_game.split('\n')[0]
       stripped_list.append(stripped_game)
      
   return stripped_list

def split_games(game_list):
    split_list = []
    for game in game_list:
        stripped_game = game.split('; ')
        g_list = []
        for g in stripped_game:
            stripped_g = g.split(', ')
            g_list.append(stripped_g)
        split_list.append(g_list)
    return split_list
        
    

lines = strip_game_numbers(lines)
lines = split_games(lines)
all_games = 0
total = 0


for n, game in enumerate(lines):
    cubes_copy = {'red': 0, 'green':0, 'blue':0}
    all_games += n + 1
    valid_game = True
    for match in game:
        valid_match = True
        for color in match:
            split = color.split(" ")
            for key in cubes_copy.keys():
                if(key == split[1] and int(split[0]) > int(cubes_copy[split[1]])):
                    cubes_copy[split[1]] = split[0]
    power = 1
    for colors in cubes_copy.items():
        power *= int(colors[1])     
    total += power
   
print('Total sum of powers:', total)
        
file.close()