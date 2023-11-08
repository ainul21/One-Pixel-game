import pygame
import random
from player import Player
from enemy import Enemy

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 30
ITEMS_TO_LEVEL_UP = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Open World RPG")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Button class
class Button:
    def __init__(self, text, width, height, pos):
        self.text = text
        self.width = width
        self.height = height
        self.position = pos
        self.set_rect()
        self.draw_button()

    def set_rect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def draw_button(self):
        pygame.draw.rect(screen, BLACK, self.rect)
        font = pygame.font.SysFont(None, 36)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Item class
class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

# Function to reset the game
def reset_game():
    global GAME_OVER, player, enemies, all_sprites, item, level
    player = Player()
    enemies = pygame.sprite.Group()
    item = Item()
    all_sprites = pygame.sprite.Group(player, item)
    level = 1
    add_enemies(level)
    GAME_OVER = False

# Function to add enemies
def add_enemies(level):
    for i in range(level * 2):  # Double the number of enemies each level
        new_enemy = Enemy(player, 1 + (level - 1) * 0.5)  # Increase speed by 0.5 each level
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

# Setup
GAME_OVER = False
level = 1
reset_game()
replay_button = Button("Replay", 200, 50, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if GAME_OVER and replay_button.check_click(event):
            reset_game()

    # Update
    if not GAME_OVER:
        all_sprites.update()
        # Check for item collection
        if pygame.sprite.collide_rect(player, item):
            player.collect_item(item)
            if player.score % ITEMS_TO_LEVEL_UP == 0:
                level += 1
                add_enemies(level)
        # Check for collision with enemies
        if pygame.sprite.spritecollideany(player, enemies):
            GAME_OVER = True

    # Drawing
    screen.fill(WHITE)
    if not GAME_OVER:
        all_sprites.draw(screen)
        # Display score and level
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {player.score}', True, BLACK)
        level_text = font.render(f'Level: {level}', True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
    else:
        # Display game over message and score
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render('Game Over', True, RED)
        score_text = font.render(f'Score: {player.score}', True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        replay_button.draw_button()

    # Flip the display
    pygame.display.flip()

    # Maintain the frame rate
    clock.tick(FPS)

pygame.quit()
