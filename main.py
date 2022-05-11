import json
from sys import argv as animalInput

data = '{"canine":["perro", "lobo", "zorro", "coyote"], "feline":["gato", "tigre", "leon", "lince"],"bird":["halcon", "pinguino", "paloma", "aguila", "buitre"]}'
json_animal = json.loads(data)

"print(json.dumps(json_animal, indent=2))"
genere = None

try:
    for key in json_animal:
        for value in json_animal[key]:
            if value == animalInput[1].lower():
                genere = key

    if genere == 'canine':
        from animal import canine as animal
    elif genere == 'feline':
        from animal import feline as animal
    elif genere == 'bird':
        from animal import bird as animal
    else:
        raise SyntaxError

    animal_object = animal(animalInput[2].lower())
    animal_object.info()
except Exception as e:
    print("Hola mundo")
