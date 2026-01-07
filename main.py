import tkinter as tk       # Librería para interfaz gráfica
import random              # Para elegir una oración aleatoria
import timeit              # Para medir el tiempo transcurrido

# -------------------------------
# Crear la ventana principal
# -------------------------------
ventana = tk.Tk()
ventana.title("Test de velocidad de escritura")
ventana.geometry("700x400")  # Tamaño de la ventana
ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño

# -------------------------------
# Lista de oraciones
# -------------------------------
oraciones = [
    'La práctica diaria mejora la velocidad al escribir',
    'Python es un lenguaje sencillo y poderoso',
    'Escribir rápido requiere paciencia y constancia',
    'El teclado es una herramienta muy importante',
    'Aprender programación desarrolla el pensamiento lógico',
    'La mecanografía ayuda a escribir con mayor precisión',
    'Programar en Python puede ser divertido y educativo',
    'La concentración es clave para evitar errores al escribir',
    'El tiempo y la precisión determinan un buen resultado',
    'Practicar todos los días mejora el rendimiento'
]

# Elegir una oración al azar
oracion_actual = random.choice(oraciones)

# -------------------------------
# Mostrar la oración en pantalla
# -------------------------------
etiqueta_oracion = tk.Label(
    ventana,
    text= oracion_actual,
    font= ("Arial", 14),
    wraplength= 650,      # Ajusta el texto si es muy largo
    justify ="center"
)
etiqueta_oracion.pack(pady=20)  # Margen vertical para separar elementos

# -------------------------------
# Caja de texto para escribir
# -------------------------------
entrada_usuario = tk.Entry(
    ventana,
    font= ("Arial", 14),
    width= 80
)
entrada_usuario.pack(pady=10)

# -------------------------------
# Variable para temporizador
# -------------------------------
tiempo_inicio = None  # Guarda el momento en que empieza a escribir (NONE para que este vacia)

# -------------------------------
# Función para iniciar el temporizador
# -------------------------------
def iniciar_tiempo(tecla):
    """
    Se llama al presionar cualquier tecla.
    Solo asigna el tiempo la primera vez.
    """
    global tiempo_inicio
    if tiempo_inicio is None:
        tiempo_inicio = timeit.default_timer()

# -------------------------------
# Función para terminar la prueba y mostrar resultados
# -------------------------------
def terminar_prueba_enter(tecla):
    """
    Se llama al presionar Enter.
    Calcula tiempo transcurrido, errores y precisión.
    Muestra resultados en etiquetas dentro de la ventana.
    Bloquea la caja de texto para que no se siga escribiendo.
    """
    global tiempo_inicio
    if tiempo_inicio is not None:
        # Tiempo final
        tiempo_final = timeit.default_timer()
        tiempo_total = tiempo_final - tiempo_inicio

        # Obtener texto del usuario
        texto_usuario = entrada_usuario.get()
        texto_original = oracion_actual

        # Comparar carácter por carácter
        caracteres_correctos = 0
        errores = 0
        for i in range(max(len(texto_usuario), len(texto_original))):
            if i < len(texto_usuario) and i < len(texto_original):
                if texto_usuario[i] == texto_original[i]:
                    caracteres_correctos += 1
                else:
                    errores += 1
            else:
                # Caracteres extra o faltantes cuentan como errores
                errores += 1

        # Calcular precisión (%)
        precision = (caracteres_correctos / len(texto_original)) * 100

        # -------------------------------
        # Mostrar resultados en la ventana
        # -------------------------------
        etiqueta_resultados = tk.Label(
            ventana,
            text=f"Tiempo: {tiempo_total:.2f} segundos\n"
                 f"Errores: {errores}\n"
                 f"Precisión: {precision:.2f}%",
            font= ("Arial", 14),
            fg= "blue",
            justify= "center"
        )
        etiqueta_resultados.pack(pady=20)

        # Bloquear la caja de texto
        entrada_usuario.config(state="disabled")

    else:
        etiqueta_resultados = tk.Label(
            ventana,
            text= "No se ha escrito nada.",
            font= ("Arial", 14),
            fg= "red"
        )
        etiqueta_resultados.pack(pady=20)

# -------------------------------
# Llamamos a nuestras funciones
# -------------------------------
entrada_usuario.bind("<Key>", iniciar_tiempo)           # Inicia temporizador con la primera tecla
entrada_usuario.bind("<Return>", terminar_prueba_enter) # Termina prueba al presionar Enter

# -------------------------------
# Ejecutar la ventana
# -------------------------------
ventana.mainloop()

