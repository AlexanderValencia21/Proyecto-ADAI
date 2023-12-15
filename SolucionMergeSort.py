import time

class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza

    def __str__(self):
        return f"{self.nombre} ({self.grandeza})"


class Escena:
    def __init__(self, animales):
        self.animales = self.ordenar_animales_mergesort(animales)
        self.grandeza_total = sum(animal.grandeza for animal in self.animales)
        self.max_grandeza_individual = max(animal.grandeza for animal in self.animales)

    def __str__(self):
        return ", ".join(str(animal) for animal in self.animales)

    def ordenar_animales_mergesort(self, animales):
        if len(animales) <= 1:
            return animales

        medio = len(animales) // 2
        izquierda = animales[:medio]
        derecha = animales[medio:]

        izquierda = self.ordenar_animales_mergesort(izquierda)
        derecha = self.ordenar_animales_mergesort(derecha)

        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].grandeza <= derecha[j].grandeza:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado


class Espectaculo:
    def __init__(self, n, m, k, animales, apertura, partes):
        self.n = n
        self.m = m
        self.k = k
        self.animales = animales
        self.apertura = [Escena([animal for animal in escena]) for escena in apertura]
        self.partes = [
            [Escena([animal for animal in partida]) for partida in parte] for parte in partes
        ]

    def mergesort_order(self, escenas):
        if len(escenas) <= 1:
            return escenas

        medio = len(escenas) // 2
        izquierda = escenas[:medio]
        derecha = escenas[medio:]
        izquierda = self.mergesort_order(izquierda)
        derecha = self.mergesort_order(derecha)

        return self.merge(izquierda, derecha)

    def merge(self, izquierda, derecha):
        resultado = []
        i = j = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i].grandeza_total <= derecha[j].grandeza_total:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1

        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])

        return resultado

    def show(self, escenas):
        for escena in escenas:
            print(escena)

    def iniciar_show(self):
        orden_aper = self.mergesort_order(self.apertura)
        order_part = [self.mergesort_order(parte) for parte in self.partes]

        print("Apertura:")
        self.show(orden_aper)
        print()

        for i, parte in enumerate(order_part, 1):
            print(f"Parte {i}:")
            self.show(parte)
            print()

        escenas_ordenadas = orden_aper + sum(order_part, [])
        animales_escenas = [
            animal for escena in escenas_ordenadas for animal in escena.animales
        ]

        animales_participantes = set(animales_escenas)
        cont_animal = {
            animal: animales_escenas.count(animal) for animal in animales_participantes
        }

        animal_mas_participante = max(cont_animal, key=cont_animal.get)
        max_participacion = cont_animal[animal_mas_participante]

        animales_menos_participantes = [
            animal
            for animal, count in cont_animal.items()
            if count == min(cont_animal.values())
        ]
        min_participacion = cont_animal[animales_menos_participantes[0]]

        escena_menor_grandeza = min(
            escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )
        escena_mayor_grandeza = max(
            escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )

        promedio_grandezas = sum(animal.grandeza for animal in animales_escenas) / len(escenas_ordenadas)


        print("\nResultados:")
        print(
            f"El animal que participó en más escenas dentro del espectáculo fue {animal_mas_participante.nombre} que participó en {max_participacion} escenas."
        )
        print(
            f"El animal que menos participó en escenas dentro del espectáculo fueron {', '.join(animal.nombre for animal in animales_menos_participantes)} quienes participaron cada uno en {min_participacion} escenas."
        )
        print(
            f"La escena de menor grandeza fue la escena {escena_menor_grandeza}."
        )
        print(
            f"La escena de mayor grandeza fue la escena {escena_mayor_grandeza}."
        )
        print(
            f"El promedio de grandeza en todo el espectáculo fue de {promedio_grandezas:.2f}."
        )

    def tiempo(self):
        inicio = time.time()
        self.iniciar_show()
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos.")


#Aqui probamos el algortimo
n = 9
m = 4
k = 3

list_animal = {
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

capibara = list_animal["Capibara"]
loro = list_animal["Loro"]
caiman = list_animal["Caimán"]
boa = list_animal["Boa"]
cocodrilo = list_animal["Cocodrilo"]
cebra = list_animal["Cebra"]
pantera = list_animal["Pantera negra"]
tigre = list_animal["Tigre"]
leon = list_animal["León"]

list_apertura = [
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

list_partes = [
    [[caiman, capibara, loro], [tigre, loro, capibara], [tigre, cebra, pantera]],
    [[pantera, cocodrilo, loro], [leon, pantera, cebra], [cocodrilo, capibara, loro]],
    [[boa, caiman, capibara], [leon, caiman, loro], [leon, cocodrilo, boa]],
]

espectaculo = Espectaculo(n, m, k, list_animal, list_apertura, list_partes)

# Ejecución del espectáculo
espectaculo.tiempo()
