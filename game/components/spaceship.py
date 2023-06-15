import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, SPACESHIP_BULLET
from pygame.sprite import Sprite

# Clase para la nave espacial
class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]
        self.bullets = pygame.sprite.Group()
        self.shoot_delay = 200
        self.last_shot_time = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image_rect.x -= 7
        if self.image_rect.right < 0:
            self.image_rect.left = SCREEN_WIDTH
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image_rect.x += 7
        if self.image_rect.left > SCREEN_WIDTH:
            self.image_rect.right = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.image_rect.y -= 7
        if self.image_rect.top < 0:
            self.image_rect.top = 0
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.image_rect.y += 7
        if self.image_rect.bottom > SCREEN_HEIGHT:
            self.image_rect.bottom = SCREEN_HEIGHT

        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_delay:
            self.shoot()
            self.last_shot_time = current_time

        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        self.bullets.draw(screen)

    def shoot(self):
        bullet = Bullet(self.image_rect.midtop)
        self.bullets.add(bullet)


# Clase para la bala
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = SPACESHIP_BULLET
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
