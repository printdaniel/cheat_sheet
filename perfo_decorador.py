#######################
# Decorador para perfo
#######################
"""En Python, un decorador es una función que toma otra función como entrada, 
y devuelve una nueva función como salida. El decorador actúa como un 
envoltorio (wrapper) alrededor de la función original, añadiendo alguna 
funcionalidad adicional sin modificar la función original.

Los decoradores se utilizan para modificar el comportamiento de una función 
sin tener que cambiar su código. Se pueden utilizar para agregar 
funcionalidades a una función existente, como medición del tiempo de 
ejecución, validación de parámetros, manejo de excepciones, autenticación 
y autorización, y muchos otros propósitos."""

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(
            f"La función {func.__name__} tardó {fin - inicio:.5f} segundos en ejecutarse.")
        return resultado
    return wrapper


@medir_tiempo
def tiempo():
    time.sleep(3)



def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Tiempo de inicio en segundos
        result = func(*args, **kwargs)
        end_time = time.time()  # Tiempo de finalización en segundos
        execution_time = (end_time - start_time) * 1000  # Tiempo de ejecución en milisegundos
        print(f"La función '{func.__name__}' tardó {execution_time:.2f} milisegundos en ejecutarse.")
        return result
    return wrapper

