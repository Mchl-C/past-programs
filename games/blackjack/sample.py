import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Input")
font = pygame.font.SysFont('Arial', 32)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)

class NumberInput:
    def __init__(self, x, y, width=200, height=50):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY
        self.text = ""
        self.active = False
        self.max_length = 10  # Maximum digits allowed

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if clicking the input box
            self.active = self.rect.collidepoint(event.pos)
            self.color = BLUE if self.active else GRAY

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Submit on Enter press
                try:
                    number = float(self.text) if '.' in self.text else int(self.text)
                    print(f"Submitted number: {number}")
                    self.active = False
                    self.color = GRAY
                except ValueError:
                    print("Please enter a valid number")
            
            elif event.key == pygame.K_BACKSPACE:
                # Handle backspace
                self.text = self.text[:-1]
            
            elif event.unicode.isdigit() or (event.unicode == '.' and '.' not in self.text):
                # Only allow digits and one decimal point
                if len(self.text) < self.max_length:
                    self.text += event.unicode

    def draw(self, surface):
        # Draw the input box
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # Render the text
        text_surface = font.render(self.text, True, BLACK)
        # Center text vertically and add some padding horizontally
        surface.blit(text_surface, (self.rect.x + 10, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

        # Render cursor if active
        if self.active:
            cursor_x = self.rect.x + 10 + font.size(self.text)[0]
            pygame.draw.line(surface, BLACK, (cursor_x, self.rect.y + 10), 
                            (cursor_x, self.rect.y + self.rect.height - 10), 2)

# Create input field
number_input = NumberInput(WIDTH//2 - 100, HEIGHT//2 - 25)

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        number_input.handle_event(event)

    # Clear screen
    screen.fill(WHITE)
    
    # Draw instructions
    instruction = font.render("Click the box and enter a number, then press Enter", True, BLACK)
    screen.blit(instruction, (WIDTH//2 - instruction.get_width()//2, HEIGHT//4))
    
    # Draw input field
    number_input.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
