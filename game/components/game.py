import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SPACESHIP_BULLET
from game.components.spaceship import SpaceShip
from game.components.enemies.enemy_manager import EnemyManager

# Clase principal del juego
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = SpaceShip(20)  # Cambiar el tamaño del bullet aquí
        self.enemy_manager = EnemyManager(random.randint(1, 1))

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        else:
            print("¡Algo ocurrió para salir del juego!")
        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.update()
        self.enemy_manager.update()

        # Verificar colisiones entre balas y enemigos
        collisions = pygame.sprite.groupcollide(self.player.bullets, self.enemy_manager.enemies, True, True)

        # Verificar colisiones entre el jugador y los enemigos
        collisions = pygame.sprite.spritecollide(self.player, self.enemy_manager.enemies, True)
        if collisions:
            # Aquí puedes realizar las acciones correspondientes cuando hay una colisión con el jugador
            print("¡Colisión con el jugador!")

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        pygame.display.update()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
