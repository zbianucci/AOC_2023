file = open('part1.txt', 'r')
lines = file.readlines()
cubes = {'red': 12, 'green':13, 'blue':14}

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
impossible = 0
all_games = 0


for n, game in enumerate(lines):
    all_games += n + 1
    valid_game = True
    for match in game:
        valid_match = True
        for color in match:
            split = color.split(" ")
            for key in cubes.keys():
                if(key == split[1] and int(split[0]) > cubes[split[1]]):
                    valid_match = False
                    print('game:', int(n+1),'color:', color )
                    break
            if(not valid_match):
                valid_match = True
                valid_game = False
                break
    if (not valid_game):
        impossible += n + 1
        valid_game = True
        
possible = all_games - impossible
print('Sum:', possible)
                    
file.close()