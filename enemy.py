import pygame
import random

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, speed=1):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(600 - self.rect.height)
        self.speed = speed
        self.player = player

    def update(self):
        # Simple AI to move the enemy towards the player
        if self.rect.x < self.player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > self.player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < self.player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > self.player.rect.y:
            self.rect.y -= self.speed
