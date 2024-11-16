
# ! Analizardo de Texto
# ASDASDASD
# ASDASDASD
# ASDASDAD

def mostrar_menu():
    print("\n--- Menu del Analizador de Texto ---")
    print("1. Ingresar texto")
    print("2. Analizar texto")
    print("3. Mostrar historial de textos")
    print("4. Salir")
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

def main():
    historial_textos = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            texto = input("\nIngresa el texto a analizar: ")
            historial_textos.append(texto)
            print("Texto guardado con éxito.")
        elif opcion == "2":
            if not historial_textos:
                print("\nNo hay textos para analizar. Por favor, ingresa uno primero.")
            else:
                texto_actual = historial_textos[-1]
                analisis = analizar_texto(texto_actual)
                mostrar_resultados(analisis)
        elif opcion == "3":
            if not historial_textos:
                print("\nNo hay textos en el historial.")
            else:
                mostrar_historial(historial_textos)
        elif opcion == "4":
            print("\n¡Gracias por usar el Analizador de Texto! ")
            break
        else:
            print("\nOpción invalida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
