import time
import heapq

'''
Aqui resolvemos el problema con una estructura de datos de cola de prioridad, usando el algoritmo de ordenamiento Heapsort 
'''
class Animal:
    def __init__(self, name, magnitude):
        self.name = name
        self.magnitude = magnitude

    def __str__(self):
        return f"{self.name} ({self.magnitude})"


class Scene:
    def __init__(self, animals):
        self.animals = tuple(sorted(animals, key=lambda animal: animal.magnitude))
        self.total_magnitude = sum(animal.magnitude for animal in self.animals)
        self.max_ind_magnitude = max(animal.magnitude for animal in self.animals)

    def __lt__(self, other):
        return self.total_magnitude < other.total_magnitude

    def __str__(self):
        return ", ".join(str(animal) for animal in self.animals)


class Show:
    def __init__(self, n, m, k, animals, opening, parts):
        self.n = n
        self.m = m
        self.k = k
        self.animals = animals
        self.opening = [Scene(tuple(escena)) for escena in opening]
        self.parts = [
            [Scene(tuple(partida)) for partida in parte] for parte in parts
        ]

    def order_by_heapsort(self, scenes):
        heap = list(scenes)
        heapq.heapify(heap)
        return [heapq.heappop(heap) for _ in range(len(heap))]

    def show_scenes(self, scenes):
        for scene in scenes:
            print(scene)

    def start_show(self):
        order_opening = self.order_by_heapsort(self.opening)
        order_parts = [self.order_by_heapsort(part) for part in self.parts]

        print("Apertura:")
        self.show_scenes(order_opening)
        print()

        for i, part in enumerate(order_parts, 1):
            print(f"Parte {i}:")
            self.show_scenes(part)
            print()

        all_scenes = order_opening + sum(order_parts, [])
        animals_scenes = [
            animal for scene in all_scenes for animal in scene.animals
        ]

        animal_participation = set(animals_scenes)
        cont_animals = {
            animal: animals_scenes.count(animal) for animal in animal_participation
        }

        max_animal_parti = max(cont_animals, key=cont_animals.get)
        max_participation = cont_animals[max_animal_parti]

        min_animal_parti = [
            animal
            for animal, count in cont_animals.items()
            if count == min(cont_animals.values())
        ]
        min_participation = cont_animals[min_animal_parti[0]]

        min_magnitude_scene = min(
            all_scenes, key=lambda escena: escena.total_magnitude
        )
        max_magnitude_scene = max(
            all_scenes, key=lambda escena: escena.total_magnitude
        )

        magnitude_prom = sum(animal.magnitude for animal in animals_scenes) / len(
            animals_scenes
        )

        print("\nResultados:")
        print(
            f"El animal que participó en más escenas dentro del espectáculo fue {max_animal_parti.name} que participó en {max_participation} escenas."
        )
        print(
            f"El animal que menos participó en escenas dentro del espectáculo fueron {', '.join(animal.name for animal in min_animal_parti)} quienes participaron cada uno en {min_participation} escenas."
        )
        print(
            f"La escena de menor grandeza total fue la escena {min_magnitude_scene}."
        )
        print(
            f"La escena de mayor grandeza total fue la escena {max_magnitude_scene}."
        )
        print(
            f"El promedio de grandeza de todo el espectáculo fue de {magnitude_prom:.2f}."
        )

    def medir_tiempo(self):
        inicio = time.time()
        self.start_show()
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos.")


# Ejemplo de uso
n = 9
m = 4
k = 3

animals_list = {
    "Capibara": Animal("Capibara", 1),
    "Loro": Animal("Loro", 2),
    "Caimán": Animal("Caimán", 3),
    "Boa": Animal("Boa", 4),
    "Cocodrilo": Animal("Cocodrilo", 5),
    "Cebra": Animal("Cebra", 6),
    "Pantera negra": Animal("Pantera negra", 7),
    "Tigre": Animal("Tigre", 8),
    "León": Animal("León", 9),
}

capibara = animals_list["Capibara"]
loro = animals_list["Loro"]
caiman = animals_list["Caimán"]
boa = animals_list["Boa"]
cocodrilo = animals_list["Cocodrilo"]
cebra = animals_list["Cebra"]
pantera = animals_list["Pantera negra"]
tigre = animals_list["Tigre"]
leon = animals_list["León"]

opening_list = [
    [caiman, capibara, loro],
    [boa, caiman, capibara],
    [cocodrilo, capibara, loro],
    [pantera, cocodrilo, loro],
    [tigre, loro, capibara],
    [leon, caiman, loro],
    [leon, cocodrilo, boa],
    [leon, pantera, cebra],
    [tigre, cebra, pantera],
]

parts_list = [
    [[caiman, capibara, loro], [tigre, loro, capibara], [tigre, cebra, pantera]],
    [[pantera, cocodrilo, loro], [leon, pantera, cebra], [cocodrilo, capibara, loro]],
    [[boa, caiman, capibara], [leon, caiman, loro], [leon, cocodrilo, boa]],
]

show = Show(n, m, k, animals_list, opening_list, parts_list)

# Ejecución del espectáculo
show.medir_tiempo()
