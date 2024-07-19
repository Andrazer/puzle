class Pieza:
    def __init__(self, tipo, color, posicion, orientacion):
        self.tipo = tipo
        self.color = color
        self.posicion = posicion
        self.orientacion = orientacion

    def mover(self, direccion):
        # Implementar la lógica para mover la pieza en la dirección especificada
        pass

    def rotar(self):
        # Implementar la lógica para rotar la pieza
        pass

    def dibujar(self, superficie):
        # Implementar la lógica para dibujar la pieza en la superficie de juego
        pass

    def es_valido_movimiento(self, movimiento):
        # Implementar la lógica para comprobar si un movimiento es válido
        pass

    def es_combinable(self, otra_pieza):
        # Implementar la lógica para comprobar si la pieza se puede combinar con otra
        pass

    def combinar(self, otra_pieza):
        # Implementar la lógica para combinar la pieza con otra
        pass
