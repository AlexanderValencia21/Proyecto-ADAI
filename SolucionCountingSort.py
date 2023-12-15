import time
from collections import defaultdict


def zoo_show(n, m, k, animals, magnitude, opening, parts):
    animal_magnitude = dict(zip(animals, magnitude))

    # Función para ordenar las escenas según la grandeza del animal utilizando sorted
    def sort_scenes(scenes):
        return sorted(scenes, key=lambda x: sum(magnitude[animals.index(animal)] for animal in x))

    # Función para ordenar cada escena según la grandeza de los animales utilizando sorted
    def order_scenes(scenes):
        return [sorted(scene, key=lambda x: magnitude[animals.index(x)]) for scene in scenes]

    # Ordenar las escenas en la apertura según la grandeza total y la grandeza del animal utilizando sorted
    order_opening = order_scenes(opening)

    # Ordenar las partes siguientes según la grandeza total y la grandeza del animal utilizando sorted
    order_parts = [order_scenes(part) for part in parts]

    # Encontrar el animal que participa en más escenas
    animal_participation = defaultdict(int)
    for part in [opening] + parts:
        for scene in part:
            for animal in scene:
                animal_participation[animal] += 1

    max_participation = max(animal_participation.values())
    max_animals_participation = {animal for animal, participation in animal_participation.items() if participation == max_participation}

    # Encontrar el animal que participa en menos escenas
    min_participation = min(animal_participation.values())
    min_animal_participation = {animal for animal, participation in animal_participation.items() if participation == min_participation}

    # Calcular el promedio de las grandezas de todas las escenas
    magnitude_prom = sum(sum(magnitude[animals.index(animal)] for animal in scene) for parte in [opening] + parts) / sum(len(parte) for parte in [opening] + parts)

    # Imprimir la información obtenida
    print("El orden del espectaculo es")
    print("\nApertura :", order_opening)
    for i, part in enumerate(order_parts, start=1):
        print(f"\nparte{i} :", part)
    print("\nEl animal que participó en más escenas dentro del espectáculo fue", max_animals_participation, "con", max_participation, "escenas.")
    print("\nEl animal que participó en menos escenas dentro del espectáculo fue", min_animal_participation, "con", min_participation, "escenas.")
    print("\nLa escena de menor grandeza total fue la escena", order_opening[0])
    print("\nLa escena de mayor grandeza total fue la escena", order_opening[-1])
    print("\nEl promedio de grandeza de todo el espectáculo fue de", magnitude_prom)

# Función para medir el tiempo de ejecución de espectaculo_zoologico
def show_time(n, m, k, animals, magnitude, opening, parts):
    inicio = time.time()
    zoo_show(n, m, k, animals, magnitude, opening, parts)
    fin = time.time()
    tiempo_total = fin - inicio
    print("La función espectaculo_zoologico se ejecutó en", tiempo_total, "segundos")

# Ejemplo de uso
n = 6
m = 3
k = 2
animales = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]
apertura = [["gato", "ciempies", "libelula"], ["ciempies", "tapir", "gato"], ["tapir", "perro", "gato"], ["tapir", "nutria", "perro"]]
partes = [[["ciempies", "tapir", "gato"], ["tapir", "nutria", "perro"]], [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]]

show_time(n, m, k, animales, grandezas, apertura, partes)
