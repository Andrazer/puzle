import pygame

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 100, 0)
BLUE = (50, 150, 250)

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
    
    
class Game(object):
    def __init__(self):
        self.score = 0  # Initialize score within the class (optional)
        self.background_image = pygame.image.load("img/fondo.jpg").convert()
        self.logo = pygame.image.load("img/name.png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (200, 100))
        
        self.buttons = [
            Button("Start", (30, 430, 200, 50), BLUE, WHITE),
            Button("Quit", (30, 500, 200, 50), BLUE, WHITE)
        ]

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return done  # Exit the game loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    done = True
                    return done  # Exit the game loop with 'q' press
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in self.buttons:
                    if button.is_clicked(mouse_pos):
                        if button.text == "Quit":
                            return True
                        elif button.text == "Start":
                            print("Start button clicked!")
        return False  # No exit event detected

    def run_logic(self):
        pass  # This method will contain game logic (currently empty)

    def display_frame(self, screen):
        # Fill the background with the defined color
        # screen.fill(FONDO_PUZZLE)
        
        # Draw the background image
        screen.blit(self.  background_image, [0, 0])
        screen.blit(self.  logo, [30, 30])
        
        border_color = (255, 255, 255)  # White color for the border
        pygame.draw.rect(screen, border_color, zona_juego.inflate(5, 5))
        
        pygame.draw.rect(screen, border_color, zona_juego.inflate(5, 5))

        # Draw the game zone rectangle
        pygame.draw.rect(screen, (0, 0, 0), zona_juego)  # Color of the zone
        
        # Draw buttons
        for button in self.buttons:
            button.draw(screen)
            
        # Update the display with what has been drawn
        pygame.display.flip()
        

def main():
    
    game = Game()
    # Set up the game clock
    clock = pygame.time.Clock()

    # Flag to track game loop termination
    done = False

    while not done:
        # Handle game events
        done = game.process_events()

        # Update game logic (currently empty)
        game.run_logic()

        # Draw the game frame
        game.display_frame(screen)

        # Limit frame rate to 60 FPS for smooth gameplay
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
