#Funciones.py

def nombre_valido(nombre):
    if len(nombre) < 3:
        return False
    for c in nombre:
        if not (c.isalpha() or c == ' '):
            return False
    return True

def suma(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def ingresar_participantes():
    participantes = []
    print("Ingrese los nombres de 5 participantes:")
    i = 0
    while i < 5:
        nombre = input(f"Participante {i+1}: ").strip()
        if nombre_valido(nombre):
            participantes = participantes + [nombre]  # evito usar append lo reemplazo por +
            i += 1
        else:
            print("Nombre inválido. Debe tener al menos 3 caracteres y solo contener letras y espacios.")
    return participantes

def ingresar_puntuaciones(participantes, jurados=3):
    puntuaciones = []
    print("\nIngrese las puntuaciones del jurado (entre 1 y 10):")
    i = 0
    while i < len(participantes):
        nombre = participantes[i]
        print(f"\nPuntuaciones para {nombre}:")
        puntajes = []
        jurado = 0
        while jurado < jurados:
            try:
                nota = int(input(f"  Jurado {jurado+1}: "))
                if 1 <= nota <= 10:
                    puntajes = puntajes + [nota]  # evito usar append lo reemplazo por +
                    jurado += 1
                else:
                    print("  La nota debe estar entre 1 y 10.")
            except ValueError:
                print("  Entrada inválida. Debe ser un número.")
        puntuaciones = puntuaciones + [puntajes]  # evito usar append lo reemplazo por +
        i += 1
    return puntuaciones

def mostrar_resultados(participantes, puntuaciones):
    print("\n--- Resultados Finales ---\n")
    i = 0
    while i < len(participantes):
        nombre = participantes[i]
        puntajes = puntuaciones[i]
        total = suma(puntajes)
        promedio = total / len(puntajes)
        puntajes_texto = ", ".join(str(p) for p in puntajes) 
        #Une todos los strings generados con , como separador.
        print(f"{nombre:<20} Puntajes: [{puntajes_texto}]  Promedio: {promedio:.2f}")
        i += 1

def mostrar_promedios_menores(participantes, puntuaciones, limite):
    print(f"\n--- Participantes con promedio menor a {limite} ---")
    encontrados = False
    i = 0
    while i < len(participantes):
        puntajes = puntuaciones[i]
        total = 0
        jurado = 0
        while jurado < len(puntajes):
            total += puntajes[jurado]
            jurado += 1
        promedio = total / len(puntajes)

        if promedio < limite:
            print(f"{participantes[i]} - Promedio: {promedio:.2f}")
            encontrados = True
        i += 1
    if not encontrados:
        print(f"Ningún participante tuvo un promedio menor a {limite}.")

def mostrar_promedio_por_jurado(puntuaciones):
    print("\n--- Promedio por jurado ---")
    num_jurados = len(puntuaciones[0])
    num_participantes = len(puntuaciones)

    jurado = 0
    while jurado < num_jurados:
        suma_jurado = 0
        i = 0
        while i < num_participantes:
            suma_jurado += puntuaciones[i][jurado]
            i += 1
        promedio = suma_jurado / num_participantes
        print(f"Jurado {jurado+1}: {promedio:.2f}")
        jurado += 1

def mostrar_jurado_extremos(puntuaciones):
    num_jurados = len(puntuaciones[0])
    num_participantes = len(puntuaciones)

    jurado = 0
    min_promedio = None
    max_promedio = None
    jurado_mas_estricto = -1
    jurado_mas_generoso = -1

    while jurado < num_jurados:
        suma = 0
        i = 0
        while i < num_participantes:
            suma += puntuaciones[i][jurado]
            i += 1
        promedio = suma / num_participantes

        if min_promedio is None or promedio < min_promedio:
            min_promedio = promedio
            jurado_mas_estricto = jurado

        if max_promedio is None or promedio > max_promedio:
            max_promedio = promedio
            jurado_mas_generoso = jurado

        jurado += 1

    print(f"\nJurado más estricto: Jurado {jurado_mas_estricto + 1} (Promedio: {min_promedio:.2f})")
    print(f"Jurado más generoso: Jurado {jurado_mas_generoso + 1} (Promedio: {max_promedio:.2f})")

def mostrar_puntuaciones_iguales(participantes, puntuaciones):
    print("\n--- Participantes con puntuaciones iguales ---")
    encontrados = False
    i = 0
    while i < len(puntuaciones):
        nota1 = puntuaciones[i][0]
        iguales = True
        jurado = 1
        while jurado < len(puntuaciones[i]):
            if puntuaciones[i][jurado] != nota1:
                iguales = False
            jurado += 1
        if iguales:
            print(f"{participantes[i]} - Puntuaciones: {nota1}, {nota1}, {nota1}")
            encontrados = True
        i += 1
    if not encontrados:
        print("ERROR! No hay participantes con misma puntuacion. ")

def buscar_participante(participantes, puntuaciones):
    print("\n--- Buscar participante por nombre ---")
    nombre_buscado = input("Ingrese el nombre a buscar: ").strip()

    i = 0
    encontrado = False
    while i < len(participantes):
        if participantes[i].lower() == nombre_buscado.lower():
            puntajes = puntuaciones[i]
            total = 0
            jurado = 0
            while jurado < len(puntajes):
                total += puntajes[jurado]
                jurado += 1
            promedio = total / len(puntajes)
            print(f"\n{participantes[i]}:")
            print(f"Puntuaciones: {puntajes[0]}, {puntajes[1]}, {puntajes[2]}")
            print(f"Promedio: {promedio:.2f}")
            encontrado = True
            break
        i += 1

    if not encontrado:
        print("ERROR! Participante no encontrado.")

#TOP 3: Mostrar los 3 participantes con mayor puntaje. (Punto 11)
def top_3_participantes(participantes, puntuaciones):
    print("\n--- Top 3 participantes por promedio ---")
    # Crear listas paralelas de nombres y promedios
    nombres = []
    promedios = []
    i = 0
    while i < len(participantes):
        total = 0
        jurado = 0
        while jurado < len(puntuaciones[i]):
            total += puntuaciones[i][jurado]
            jurado += 1
        promedio = total / len(puntuaciones[i])
        nombres = nombres + [participantes[i]]
        promedios = promedios + [promedio]
        i += 1  
    n = len(promedios)  # Ordenar promedios y nombres de mayor a menor (selección directa)
    x = 0
    while x < n - 1:
        max_idx = x
        y = x + 1
        while y < n:
            if promedios[y] > promedios[max_idx]:
                max_idx = y
            y += 1        
        temp_prom = promedios[x] # Intercambio manual
        promedios[x] = promedios[max_idx]
        promedios[max_idx] = temp_prom

        temp_nombre = nombres[x]
        nombres[x] = nombres[max_idx]
        nombres[max_idx] = temp_nombre
        x += 1   
    limite = 3 if len(nombres) >= 3 else len(nombres) # Mostrar top 3
    k = 0
    while k < limite:
        print(f"{k+1}. {nombres[k]} - Promedio: {promedios[k]:.2f}")
        k += 1

# Participantes ordenados alfabeticamente(A-Z)con sus datos(Punto 12)
def mostrar_orden_alfabetico(participantes, puntuaciones):
    print("\n--- Participantes ordenados alfabéticamente ---")
    nombres = []
    puntos = []
    i = 0
    while i < len(participantes):
        nombres = nombres + [participantes[i]]
        puntos = puntos + [puntuaciones[i]]
        i += 1    
    n = len(nombres) # Orden alfabético manual (selección directa)
    i = 0
    while i < n - 1:
        min_idx = i
        jurado = i + 1
        while jurado < n:
            if nombres[jurado].lower() < nombres[min_idx].lower():
                min_idx = jurado
            jurado += 1

        # Intercambio nombres
        temp_nombre = nombres[i]
        nombres[i] = nombres[min_idx]
        nombres[min_idx] = temp_nombre

        # Intercambio puntuaciones
        temp_puntaje = puntos[i]
        puntos[i] = puntos[min_idx]
        puntos[min_idx] = temp_puntaje

        i += 1

    # Mostrar resultados
    i = 0
    while i < n:
        total = 0
        jurado = 0
        while jurado < len(puntos[i]):
            total += puntos[i][jurado]
            jurado += 1
        promedio = total / len(puntos[i])
        puntajes_texto = ", ".join(str(p) for p in puntos[i])
        print(f"{nombres[i]:<20} Puntajes: [{puntajes_texto}]  Promedio: {promedio:.2f}")
        i += 1

#Mostrar Ganador, si hay mas de uno informar por msj que tiene que haber desempate.(Punto 13)
def mostrar_ganador(participantes, puntuaciones):
    print("\n--- 🏆Ganador de la competencia🏆 ---")

    mejores = []
    mejores_promedios = []
    mayor_promedio = None

    i = 0
    while i < len(participantes):
        total = 0
        jurado = 0
        while jurado < len(puntuaciones[i]):
            total += puntuaciones[i][jurado]
            jurado += 1
        promedio = total / len(puntuaciones[i])

        if mayor_promedio is None or promedio > mayor_promedio:
            mayor_promedio = promedio
            mejores = [participantes[i]]
            mejores_promedios = [promedio]
        elif promedio == mayor_promedio:
            mejores = mejores + [participantes[i]]
            mejores_promedios = mejores_promedios + [promedio]
        i += 1

    if len(mejores) == 1:
        print(f"Ganador: {mejores[0]} con un promedio de {mayor_promedio:.2f}")
    else:
        print("Empate entre:")
        k = 0
        while k < len(mejores):
            print(f"- {mejores[k]} (Promedio: {mayor_promedio:.2f})")
            k += 1
        print("Debe realizarse un desempate.")

#Desempatar aleatoriamente entre los ganadores(Punto 14)
import random

def desempatar(participantes, puntuaciones):
    print("\n--- Desempate ---")

    mejores = []
    mayor_promedio = None

    i = 0
    while i < len(participantes):
        total = 0
        jurado = 0
        while jurado < len(puntuaciones[i]):
            total += puntuaciones[i][jurado]
            jurado += 1
        promedio = total / len(puntuaciones[i])

        if mayor_promedio is None or promedio > mayor_promedio:
            mayor_promedio = promedio
            mejores = [participantes[i]]
        elif promedio == mayor_promedio:
            mejores = mejores + [participantes[i]]
        i += 1

    if len(mejores) == 1:
        print("No hay empate, no es necesario desempatar.")
    else:
        elegido = random.choice(mejores)
        print("Ganadores empatados:")
        k = 0
        while k < len(mejores):
            print(f"- {mejores[k]}")
            k += 1
        print(f"\n Ganador elegido por desempate: {elegido}")