def mostrar_menu():
    print("\n🎵 Simulador de Spotify 🎵")
    print("1. Reproducir canción actual")
    print("2. Siguiente canción")
    print("3. Canción anterior")
    print("4. Mostrar lista de canciones")
    print("5. Salir")

# Lista de reproducción (Lista de strings)
playlist = [
    "Coldplay - Viva La Vida",
    "Daft Punk - One More Time",
    "The Beatles - Hey Jude",
    "Queen - Bohemian Rhapsody",
    "Adele - Rolling in the Deep"
]

indice_actual = 0  # Índice de la canción actual

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        print(f"\n▶️ Reproduciendo: {playlist[indice_actual]}")
    elif opcion == "2":
        if indice_actual < len(playlist) - 1:
            indice_actual += 1
            print(f"\n⏭️ Siguiente canción: {playlist[indice_actual]}")
        else:
            print("\n🚫 No hay más canciones en la lista.")
    elif opcion == "3":
        if indice_actual > 0:
            indice_actual -= 1
            print(f"\n⏮️ Volviendo a: {playlist[indice_actual]}")
        else:
            print("\n🚫 Ya estás en la primera canción.")
    elif opcion == "4":
        print("\n📜 Lista de reproducción:")
        for i, cancion in enumerate(playlist):
            indicador = "🎵" if i == indice_actual else "  "
            print(f"{indicador} {i + 1}. {cancion}")
    elif opcion == "5":
        print("\n👋 Cerrando el simulador de Spotify. ¡Hasta luego!")
        break
    else:
        print("\n⚠️ Opción inválida, intenta de nuevo.")

