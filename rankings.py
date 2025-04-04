class Game:
    def __init__(self, name, console):
        self.name = name
        self.rating = 0.0
        self.algorithmRating = 0
        self.console = console

    def setRating(self, rating):
        self.rating = rating

    def setAlgorithmRating(self, algorithmRating):
        self.algorithmRating = algorithmRating

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


def create_games_list(consoles_games):
    for console in consoles_games:
        print("Enter 5 games you rank top:")
        print("Console: " + console)
        finished = False
        i = 1
        games_list = []
        while not finished:
            item = input(str(i) + ": ")
            game = Game(item, console)
            games_list.append(game)
            i += 1

            if i > 5:
                while True:
                    print("Your games:", games_list)
                    inp = input("Is your list okay? Y/N: ")
                    if inp.lower() == 'y':
                        finished = True
                        i = 1
                        consoles_games[console] = games_list
                        break
                    elif inp.lower() == 'n':
                        i = 1
                        games_list = []
                        break
                    else:
                        print("Please enter Y or N.")


def give_games_ratings(consoles_games):
    for console in consoles_games:
        print("Give a rating for each game.")
        for game in consoles_games[console]:
            while True:
                try:
                    rating = float(input(game.name + ": "))
                    if rating > 10.0:
                        rating = 10.0
                    game.setRating(rating)
                    break
                except ValueError:
                    print("Please enter a valid number.")


def break_ties(fullList):
    ties = [fullList[0]]
    brokenTieList = []
    n = len(fullList)

    for i in range(1, n):
        current = fullList[i]
        prev = fullList[i - 1]

        if current.rating == prev.rating:
            ties.append(current)
        else:
            if len(ties) > 1:
                print("Detected ties — please compare the following:")
                for j in range(len(ties)):
                    for k in range(j + 1, len(ties)):
                        done = False
                        while not done:
                            result = input(f"1: {ties[j].name} or 2: {ties[k].name}? ")
                            if result == "1":
                                ties[j].algorithmRating += 1
                                ties[k].algorithmRating -= 1
                                done = True
                            elif result == "2":
                                ties[k].algorithmRating += 1
                                ties[j].algorithmRating -= 1
                                done = True
                            else:
                                print("Invalid input. Enter 1 or 2.")
                ties.sort(key=lambda game: game.algorithmRating, reverse=True)

            brokenTieList.extend(ties)
            ties = [current]

    # Add final tie group
    if ties:
        if len(ties) > 1:
            print("Detected ties — please compare the following:")
            for j in range(len(ties)):
                for k in range(j + 1, len(ties)):
                    done = False
                    while not done:
                        result = input(f"1: {ties[j].name} or 2: {ties[k].name}? ")
                        if result == "1":
                            ties[j].algorithmRating += 1
                            ties[k].algorithmRating -= 1
                            done = True
                        elif result == "2":
                            ties[k].algorithmRating += 1
                            ties[j].algorithmRating -= 1
                            done = True
                        else:
                            print("Invalid input. Enter 1 or 2.")
            ties.sort(key=lambda game: game.algorithmRating, reverse=True)

        brokenTieList.extend(ties)

    return brokenTieList


def assign_algorithm_ratings(consoles_games):
    fullList = []
    for console in consoles_games:
        for game in consoles_games[console]:
            fullList.append(game)

    fullList.sort(key=lambda g: g.rating, reverse=True)
    return break_ties(fullList)

def assign_console_ratings(ratingsList):
    consoles = { "N64": 0, "GB/GBA": 0, "DS/DSi" : 0, "3DS": 0, "Wii": 0, "GameCube": 0, "Switch": 0 }

    
    for i in range(len(ratingsList)):
        rating = i + 1  
        consoles[ratingsList[i].console] += rating


    console_counts = {key: 0 for key in consoles}
    for game in ratingsList:
        console_counts[game.console] += 1

    for console in consoles:
        if console_counts[console] > 0:
            consoles[console] /= console_counts[console]

    tierList = sorted(consoles.items(), key=lambda x: x[1])  
    return tierList


def print_final_results(sorted_games, tierList):
    print("Sorted Games:")
    for idx, game in enumerate(sorted_games, start=1):
        print(f"{idx}. {game.name}")
    
    print("\nConsole Ratings:")
    for idx, (console, rating) in enumerate(tierList, start=1):
        print(f"{idx}. {console}: {rating}")
    
    


consoles_games = { "N64": [], "GB/GBA": [], "DS/DSi" : [], "3DS": [], "Wii": [], "GameCube": [], "Switch": [] }
""" 
sorted_games = [
    Game("FE Radiant Dawn", "Wii"),
    Game("Breath of the Wild", "Switch"),
    Game("FE Path of Radiance", "GameCube"),
    Game("FE Three Houses", "Switch"),
    Game("Zelda Twilight Princess", "Wii"),
    Game("SSB Ultimate", "Switch"),
    Game("PMD Red Rescue Team", "GB/GBA"),
    Game("Pokemon D/P/Pt", "DS/DSi"),
    Game("Zelda Wind Waker", "GameCube"),
    Game("Mii Streetpass", "3DS"),
    Game("SSB Brawl", "Wii"),
    Game("SSB Melee", "GameCube"),
    Game("Ocarina of Time", "N64"),
    Game("FE Engage", "Switch"),
    Game("Majora's Mask", "N64"),
    Game("FE Shadows of Valentia", "3DS"),
    Game("Pokemon OR/AS", "3DS"),
    Game("Wii Sports Resort", "Wii"),
    Game("Wii Sports", "Wii"),
    Game("Fire Emblem Awakening", "3DS"),
    Game("Pokemon Ranger", "DS/DSi"),
    Game("Fire Emblem 7", "GB/GBA"),
    Game("Pokemon X/Y", "3DS"),
    Game("Pokemon G/S/C", "GB/GBA"),
    Game("MK DoubleDash", "GameCube"),
    Game("Sacred Stones", "GB/GBA"),
    Game("MK8", "Switch"),
    Game("MK Super Circuit", "GB/GBA"),
    Game("Pokemon Snap", "N64"),
    Game("Smash 64", "N64"),
    Game("Kirby 64", "N64"),
    Game("PMD Sky Explorers", "DS/DSi"),
    Game("Skyward Sword", "Wii"),
    Game("Sonic Rush", "DS/DSi"),
    Game("Mario Party DS", "DS/DSi")
]
"""


create_games_list(consoles_games)
give_games_ratings(consoles_games)
final = assign_algorithm_ratings(consoles_games)

console_ratings = assign_console_ratings(final)

print_final_results(final, console_ratings)
