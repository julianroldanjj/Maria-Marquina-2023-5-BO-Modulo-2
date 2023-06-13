import pygame.sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Tecla A o Flecha izquierda para moverse a la izquierda
            self.image_rect.x -= 7
        if self.image_rect.right < 0:
            self.image_rect.left = SCREEN_WIDTH
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Tecla D o Flecha derecha para moverse a la derecha
            self.image_rect.x += 7
        if self.image_rect.left > SCREEN_WIDTH:
            self.image_rect.right = 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Tecla W o Flecha arriba para moverse hacia arriba
            self.image_rect.y -= 7
        if self.image_rect.top < 0:
            self.image_rect.top = 0
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Tecla S o Flecha abajo para moverse hacia abajo
            self.image_rect.y += 7
        if self.image_rect.bottom > SCREEN_HEIGHT:
            self.image_rect.bottom = SCREEN_HEIGHT
