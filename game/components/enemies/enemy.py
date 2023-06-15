import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550] 
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    MOV_X = {0: "left", 1: "right"}
    RAND_IMAGE = [ENEMY_1, ENEMY_2]

    def __init__(self):
        super().__init__()
        self.image = random.choice(self.RAND_IMAGE)
        self.image = pygame.transform.scale(self.image, (random.randint(40, 80), random.randint(60, 100)))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.typo = "enemy"

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = random.choice(list(self.MOV_X.values()))
        self.movement_x_for = random.randint(30, 200)
        self.index = 0
        self.shooting_time = random.randint(30, 50)

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.movement_x_for and self.movement_x == "right") or (self.rect.x >= (SCREEN_WIDTH - 40)):
            self.movement_x = "left"
        elif (self.index >= self.movement_x_for and self.movement_x == "left") or (self.rect.x <= 10):
            self.movement_x = "right"

        if self.index >= self.movement_x_for:
            self.index = 0

    def update(self):
        self.rect.y += self.speed_y

        if self.movement_x == "left":
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
