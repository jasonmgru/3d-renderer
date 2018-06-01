import pygame
import numpy as np

import settings
import maps
import clickable
import button
import wireframebox as wfb
from colors import *

class Viewer:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()

        self._clickables = []
        self._wireframes = []
        self._transformations = {}

        self._keymap = maps.keymap
        self._state_keymap = maps.state_keymap
        self._eventmap = maps.eventmap
        self._set = settings.Settings(pygame, self, width, height)
        self._screen = pygame.display.set_mode( \
                                    (self._set.width, self._set.height), \
                                    self._set.full() \
                                    )
        self._clock = pygame.time.Clock()

    def add_wireframe(self, wireframe):
        self._wireframes.append(wireframe)
        self._clickables.append(wfb.WireframeBox(wireframe))

    def add_clickable(self, clickable):
        self._clickables.append(clickable)

    def run(self):
        while self._set.running:
            for event in pygame.event.get():
                if event.type in self._eventmap.keys():
                    self._eventmap[event.type](self, event)
                            
            for t in self._transformations.values():
                t(self)
            for h in self._clickables:
                h.update(pygame.mouse.get_pos())
            self._display()
        
        pygame.font.quit()
        pygame.quit()

    def _keydown(self, key):
        if key in self._keymap.keys():
            self._transformations[key] = self._keymap[key]
        elif key in self._state_keymap.keys():
            self._state_keymap[key](self, True)

    def _keyup(self, key):
        if key in self._transformations.keys():
            del self._transformations[key]
        elif key in self._state_keymap.keys():
            self._state_keymap[key](self, False)

    def _mousedown(self, button):
        for h in self._clickables:
            if h.hovering():
                h.press()
                break

    def _mouseup(self, button):
        if not self._set.shifted:
            self._deselect()
        for h in self._clickables:
            if h.hovering():
                h.release()
                break

    def _deselect(self):
        for wf in self._wireframes:
            wf.set_selected(False)

    def _set_running(self, running_bool):
        self._set.running = running_bool

    def _set_shifted(self, shifted_bool):
        self._set.shifted = shifted_bool

    def _display(self):
        self._screen.fill(BACKGROUND)
        self._draw_wireframes()
        rect = (0, 0, 50, self._set.height)
        pygame.draw.rect(self._screen, MENU, rect)
        pygame.draw.rect(self._screen, BUTTONS, rect, 1)
        self._draw_clickables()
        self._draw_cursor()
        pygame.display.flip()
        self._clock.tick(60)

    def _draw_wireframes(self):
        for wf in self._wireframes:
            nodes = wf.nodes()
            faces = wf.faces()
            if self._set.display_faces:
                for f in faces:
                    if wf.perp(f)[2] < 0:
                        points = wf.get_points(f, 2)
                        pygame.draw.polygon(self._screen, f[3], points)
                        if wf.selected():
                            pygame.draw.aalines(self._screen, YELLOW, \
                                              True, points)

    def _draw_clickables(self):
        for c in self._clickables:
            if c.visible():
                self._screen.blit(c.img(), c.rect())
            if c.hovering():
                pygame.draw.rect(self._screen, YELLOW, c.rect(), 1)

    def _draw_cursor(self):
        cursor_pos = pygame.mouse.get_pos()
        pygame.draw.circle(self._screen, YELLOW, cursor_pos, 3, 1)

    def _translate_selected(self, dx, dy, dz):
        for wf in self._wireframes:
            if wf.selected():
                wf.translate(dx, dy, dz)

    def _scale_selected(self, sx, sy, sz):
        for wf in self._wireframes:
            if wf.selected():
                wf.scale(sx, sy, sz)

    def _rotate_selected(self, axis, angle):
        for wf in self._wireframes:
            if wf.selected():
                rotate_fun = getattr(wf, "rotate_"+axis)
                rotate_fun(angle)
