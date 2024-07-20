import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
BLUE = (50, 150, 250)
MARRON = (180, 80, 50)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FONDO_PUZZLE = (0, 100, 0)  # Green background color
MARCO = (256, 256, 256)  # Should be (255, 255, 255) for white color

# Initialize Pygame
pygame.init()

# Create the game screen with a title
pygame.display.set_caption("Mi juego de puzles")
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Define the game zone as a rectangle
zona_juego = pygame.Rect(250, 50, 600, 500)  # Position (x, y) and dimensions
zona_previa = pygame.Rect(30, 180, 200, 200)

# Define the font for the buttons
font = pygame.font.Font(None, 36)  # Use a default font with size 36

class Button:
    def __init__(self, text, rect, color, text_color):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.color = color
        self.text_color = text_color
        self.text_surface = font.render(text, True, text_color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Pieza:
    def __init__(self, tipo, color, posicion, orientacion):
        self.tipo = tipo
        self.color = color
        self.posicion = posicion
        self.orientacion = orientacion

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.posicion)

    def move(self, dx, dy):
        self.posicion = self.posicion.move(dx, dy)

class Game:
    def __init__(self):
        self.score = 0
        self.background_image = pygame.image.load("img/fondo.jpg").convert()
        self.logo = pygame.image.load("img/puzle.jpeg").convert()
        self.logo = pygame.transform.scale(self.logo, (200, 100))
        
        self.buttons = [
            Button("Start", (30, 430, 200, 50), MARRON, WHITE),
            Button("Quit", (30, 500, 200, 50), MARRON, WHITE)
        ]
        
        self.pieza_previa = self.create_new_piece()
        self.piezas = [self.pieza_previa]
        self.placed_pieces = []
        self.selected_piece = None

    def create_new_piece(self):
        color = random.choice([BLUE, MARRON])
        return Pieza("cuadrado", color, pygame.Rect(70, 220, 120, 120), 0)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in self.buttons:
                    if button.is_clicked(mouse_pos):
                        if button.text == "Quit":
                            return True
                        elif button.text == "Start":
                            print("Start button clicked!")
                for pieza in self.piezas:
                    if pieza.posicion.collidepoint(mouse_pos):
                        self.selected_piece = pieza
                        break
            if event.type == pygame.MOUSEBUTTONUP:
                if self.selected_piece:
                    if self.snap_piece_to_grid(self.selected_piece):
                        self.piezas.append(self.create_new_piece())
                    self.selected_piece = None
            if event.type == pygame.MOUSEMOTION:
                if self.selected_piece:
                    dx, dy = event.rel
                    self.selected_piece.move(dx, dy)
        return False

    def snap_piece_to_grid(self, pieza):
        x, y, width, height = pieza.posicion
        x = ((x - zona_juego.x) // 120) * 120 + zona_juego.x
        y = ((y - zona_juego.y) // 120) * 120 + zona_juego.y
        pieza.posicion.topleft = (x, y)

        if not zona_juego.contains(pieza.posicion):
            return False

        for placed_piece in self.placed_pieces:
            if pieza.posicion.colliderect(placed_piece.posicion):
                return False

        self.placed_pieces.append(pieza)
        return True

    def run_logic(self):
        pass

    def display_frame(self, screen):
        screen.blit(self.background_image, [0, 0])
        screen.blit(self.logo, [30, 30])
        
        border_color = (255, 255, 255)
        pygame.draw.rect(screen, border_color, zona_juego.inflate(5, 5))
        pygame.draw.rect(screen, border_color, zona_previa.inflate(5, 5))
        
        pygame.draw.rect(screen, (0, 0, 0), zona_previa)
        pygame.draw.rect(screen, (0, 0, 0), zona_juego)
        
        for button in self.buttons:
            button.draw(screen)
        
        for pieza in self.piezas:
            pieza.draw(screen)

        for pieza in self.placed_pieces:
            pieza.draw(screen)
        
        pygame.display.flip()

def main():
    game = Game()
    clock = pygame.time.Clock()
    done = False

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
