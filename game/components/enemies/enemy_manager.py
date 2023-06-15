import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import SCREEN_WIDTH

# Clase para el administrador de enemigos
class EnemyManager:
    def __init__(self, max_enemies):
        self.enemies = []
        self.max_enemies = max_enemies
        self.spawn_delay = 0
        self.last_spawn_time = pygame.time.get_ticks()

    def create_enemies(self, num_enemies):
        for _ in range(num_enemies):
            enemy = Enemy()
            self.enemies.append(enemy)

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def add_enemy(self):
        if len(self.enemies) < self.max_enemies:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_spawn_time > self.spawn_delay:
                enemy = Enemy()
                self.enemies.append(enemy)
                self.last_spawn_time = current_time

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
