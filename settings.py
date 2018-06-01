import pygame
import clickable
import button
from colors import *

class Settings:
    def __init__(self, pygame, viewer, width, height):
        self.pygame = pygame
        self.viewer = viewer
        self.width = width
        self.height = height

        pygame.mouse.set_visible(False)
        icon = pygame.image.load("icon.png")
        pygame.display.set_caption("3D Cube")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("3D Cube", "3D Cube")

        self.viewer.add_clickable(self._create_exit_button())
        
        self.display_faces = True
        self.fullscreen = False
        self.running = True
        self.shifted = False

    def full(self):
        return int(self.fullscreen) * pygame.FULLSCREEN + \
               int(self.fullscreen) * pygame.HWSURFACE + \
               int(self.fullscreen) * pygame.DOUBLEBUF

    def _create_exit_button(self):
        pygame.mouse.set_visible(False)
        icon = pygame.image.load("icon.png")
        pygame.display.set_caption("3D Cube")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("3D Cube", "3D Cube")

        font = pygame.font.Font(pygame.font.get_default_font(), 12)
        text = font.render("Exit", True, WHITE)
        text_rect = text.get_rect()
        exit_img = pygame.Surface([40, 15])
        exit_img_rect = exit_img.get_rect()
        exit_img.fill(EXIT)
        exit_img.blit(text, \
            ((exit_img_rect[2]-text_rect[2])/2, \
             (exit_img_rect[3]-text_rect[3])/2) \
        )
        exit_button = button.Button((5, 5, 40, 15), exit_img)
        exit_button.release = (lambda: self.viewer._set_running(False))
        return exit_button
