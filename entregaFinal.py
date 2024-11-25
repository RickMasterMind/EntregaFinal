import os

class GestorDeTextos:
    def __init__(self):
        self.historial = []

    def agregar_texto(self, texto):
        self.historial.append(texto)

    def obtener_historial(self):
        return self.historial

    def eliminar_texto(self, indice):
        if 0 <= indice < len(self.historial):
            return self.historial.pop(indice)
        else:
            raise IndexError("indice fuera de rango.")

    def guardar_en_archivo(self, archivo="historial.txt"):
        try:
            with open(archivo, "w", encoding="utf-8") as file:
                for texto in self.historial:
                    file.write(texto + "\n")
            return f"Historial guardado con exito en el archivo '{archivo}'."
        except Exception as e:
            raise Exception(f"Error al guardar el historial: {e}")

    def cargar_desde_archivo(self, archivo="historial.txt"):
        if not os.path.exists(archivo):
            raise FileNotFoundError(f"El archivo '{archivo}' no existe.")
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                self.historial = [linea.strip() for linea in file.readlines()]
            return f"Historial cargado con exito desde el archivo '{archivo}'."
        except Exception as e:
            raise Exception(f"Error al cargar el historial: {e}")


def mostrar_menu():
    print("\n--- Menu del Analizador de Texto ---")
    print("1. Ingresar texto")
    print("2. Analizar texto")
    print("3. Mostrar historial de textos")
    print("4. Eliminar un texto del historial")
    print("5. Guardar historial en archivo .txt")
    print("6. Cargar historial desde archivo .txt")
    print("7. Salir")
    return input("Selecciona una opcion: ")


def analizar_texto(texto):
    palabras = texto.split()
    total_palabras = len(palabras)
    longitudes = [len(palabra) for palabra in palabras]
    palabra_mas_comun = max(set(palabras), key=palabras.count) if palabras else None
    longitud_promedio = sum(longitudes) / total_palabras if total_palabras > 0 else 0

    return {
        "total_palabras": total_palabras,
        "palabra_mas_comun": palabra_mas_comun,
        "longitud_promedio": longitud_promedio,
        "palabras_unicas": len(set(palabras))
    }


def mostrar_resultados(analisis):
    print("\n--- Resultados del Analisis ---")
    print(f"Total de palabras: {analisis['total_palabras']}")
    print(f"Palabra mas comun: {analisis['palabra_mas_comun']}")
    print(f"Longitud promedio de palabras: {analisis['longitud_promedio']:.2f}")
    print(f"Numero de palabras unicas: {analisis['palabras_unicas']}")


def mostrar_historial(historial):
    print("\n--- Historial de Textos Analizados ---")
    for i, texto in enumerate(historial, 1):
        print(f"{i}. {texto}")


def eliminar_texto(gestor):
    if not gestor.obtener_historial():
        print("\nNo hay textos en el historial para eliminar.")
        return

    mostrar_historial(gestor.obtener_historial())
    try:
        opcion = int(input("\nSelecciona el numero del texto que deseas eliminar: "))
        eliminado = gestor.eliminar_texto(opcion - 1)
        print(f"\nTexto eliminado con exito: {eliminado}")
    except (ValueError, IndexError):
        print("\nEntrada invalida o número fuera de rango. Intenta de nuevo.")


def main():
    gestor = GestorDeTextos()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            texto = input("\nIngresa el texto a analizar: ")
            gestor.agregar_texto(texto)
            print("Texto guardado con exito.")
        elif opcion == "2":
            if not gestor.obtener_historial():
                print("\nNo hay textos para analizar. Por favor, ingresa uno primero.")
            else:
                texto_actual = gestor.obtener_historial()[-1]
                analisis = analizar_texto(texto_actual)
                mostrar_resultados(analisis)
        elif opcion == "3":
            if not gestor.obtener_historial():
                print("\nNo hay textos en el historial.")
            else:
                mostrar_historial(gestor.obtener_historial())
        elif opcion == "4":
            eliminar_texto(gestor)
        elif opcion == "5":
            try:
                mensaje = gestor.guardar_en_archivo()
                print(f"\n{mensaje}")
            except Exception as e:
                print(f"\nError: {e}")
        elif opcion == "6":
            try:
                mensaje = gestor.cargar_desde_archivo()
                print(f"\n{mensaje}")
            except Exception as e:
                print(f"\nError: {e}")
        elif opcion == "7":
            print("\nGracias por usar el Analizador de Texto!")
            break
        else:
            print("\nOpción invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()
