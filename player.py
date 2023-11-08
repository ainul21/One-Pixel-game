import pygame

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # Green color
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Starting position
        self.speed = 5
        self.score = 0
        self.level = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def collect_item(self, item):
        self.score += 1
        item.respawn()
        if self.score >= 10:
            self.level_up()

    def level_up(self):
        self.score = 0
        self.level += 1
        self.speed += 0.5
