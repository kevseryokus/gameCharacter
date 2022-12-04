character = {"name": "ninja",
             "strength": 100,
             "gun": "sword",
             "life": 100}

print("Character's Name       :{}".format(character["name"]))
print("Strength of Character  :{}".format(character["strength"]))
print("Character's Gun        :{}".format(character["gun"]))


characterSamba = {"name": "characterSamba",
                  "strength": 70,
                  "gun": "sword",
                  "life": 100}

def hit(hitter:dict,shotdown:dict):
    diminishing = hitter["strength"]
    shotdown["life"]=shotdown["life"]-diminishing

hit(character,characterSamba)
hit(characterSamba,character)

print("Character 1 life: ",character["life"])
print("CharacterSamba life: ",characterSamba["life"])