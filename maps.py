import pygame

eventmap = {
    pygame.QUIT: (lambda s, e: s._set_running(False)),
    pygame.KEYDOWN: (lambda s, e: s._keydown(e.key)),
    pygame.KEYUP: (lambda s, e: s._keyup(e.key)),
    pygame.MOUSEBUTTONDOWN: (lambda s, e: s._mousedown(e.button)),
    pygame.MOUSEBUTTONUP: (lambda s, e: s._mouseup(e.button))
}

keymap = {
    pygame.K_UP: (lambda s: s._translate_selected(0, -5, 0)),
    pygame.K_DOWN: (lambda s: s._translate_selected(0, 5, 0)),
    pygame.K_RIGHT: (lambda s: s._translate_selected(5, 0, 0)),
    pygame.K_LEFT: (lambda s: s._translate_selected(-5, 0, 0)),
    pygame.K_w: (lambda s: s._rotate_selected('x', 0.05)),
    pygame.K_s: (lambda s: s._rotate_selected('x', -0.05)),
    pygame.K_a: (lambda s: s._rotate_selected('y', 0.05)),
    pygame.K_d: (lambda s: s._rotate_selected('y', -0.05)), 
    pygame.K_e: (lambda s: s._rotate_selected('z', -0.05)),
    pygame.K_q: (lambda s: s._rotate_selected('z', 0.05)),
    pygame.K_EQUALS: (lambda s: s._scale_selected(1.02, 1.02, 1.02)),
    pygame.K_MINUS: (lambda s: s._scale_selected(0.98, 0.98, 0.98)),
    pygame.K_ESCAPE: (lambda s: s._set_running(False))
}

state_keymap = {
    pygame.K_LSHIFT: (lambda s, b: s._set_shifted(b)),
    pygame.K_RSHIFT: (lambda s, b: s._set_shifted(b))
}