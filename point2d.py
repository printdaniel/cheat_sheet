class Point2D:
    def __new__(cls, x, y):

        if isinstance(x, int) and isinstance(y,int):
            print("Creando objeto")
            return super().__new__(cls)
        else:
            raise TypeError("x and y must be integers")

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        print("Objeto Inicializado")
