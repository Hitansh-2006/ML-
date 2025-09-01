import itertools

pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground"),
}

def strongest_teams(pokedex, k):
    names = list(pokedex.keys())
    best_teams = []
    max_types = 0
    
    print(itertools.combinations(names,k))
    for team in itertools.combinations(names, k):
        combined_types = set()
        for name in team:
            combined_types.update(pokedex[name])
        
        tcount = len(combined_types)
        
        if tcount > max_types:
            max_types = tcount
            best_teams = [(team, combined_types)]
        elif tcount == max_types:
            best_teams.append((team, combined_types))
    
    return max_types, best_teams

k = int(input("Enter the number of pokemons to build the strongest team"))
max_types, best = strongest_teams(pokedex, k)

print(f"Strongest teams with k={k}:")
print(f"Maximum unique types = {max_types}\n")

for team, types in best:
    print(f"Team: {', '.join(team)}")



## 2nd CODE


def Hermione_Spell(runes: str) :
    required = set("LUMOS")
    collected_letters = set()

    for i in range(len(runes)):        
        ch = runes[i]                  
        step = i + 1                    

        upper_ch = ch.upper()           
        if upper_ch in required:
            collected_letters.add(upper_ch)

        if collected_letters == required:
            return step      


    return -1 
magic=str(input("The runes collected are:"))
result=Hermione_Spell(magic)

if result==-1:
    print("-1")
else:
    print(f"Hermione will be able to do magic at step{result}")


