import pygame

class Player:
    def __init__(self, map_data):
        self.x = 50
        self.y = 50
        self.moving = False
        self.speed = 1  # Initial speed
        self.direction = (0, 0)  # (x, y) direction vector
        self.map_data = map_data

    def update(self):
        keys = pygame.key.get_pressed()

        # Check for movement keys
        move = (0, 0)
        if keys[pygame.K_LEFT]:
            move = (-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            move = (self.speed, 0)
        if keys[pygame.K_UP]:
            move = (0, -self.speed)
        if keys[pygame.K_DOWN]:
            move = (0, self.speed)

        # Calculate the next position
        next_x = self.x + move[0]
        next_y = self.y + move[1]

        # Check for collisions with walls
        if self.is_valid_move(next_x, next_y):
            self.x = next_x
            self.y = next_y
            self.direction = move
            self.moving = True
        else:
            self.moving = False

    def is_valid_move(self, x, y):
        # Check if the next position is within map boundaries and not a wall
        if (
            0 <= x < len(self.map_data[0]) * 32 and
            0 <= y < len(self.map_data) * 32 and
            self.map_data[y // 32][x // 32] != 1
        ):
            return True
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 32, 32))

    def on_key_press(self, key):
        # Adjust the speed when a key is pressed
        if key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
            self.speed = 1

    def on_key_release(self, key):
        # Reset the speed when a key is released
        if key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
            self.speed = 0
