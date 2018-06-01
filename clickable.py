import viewer

class Clickable:
    def __init__(self):
        self._rect = (0, 0, 0, 0)
        self._hover = False
        self._visible = False
        self._img = None
        self._type = "clickable"

    def press(self):
        pass

    def release(self):
        pass

    def hovering(self):
        return self._hover

    def update(self, cursor_pos):
        dx = cursor_pos[0] - self._rect[0]
        dy = cursor_pos[1] - self._rect[1]

        if dx > 0 and dy > 0 and dx < self._rect[2] and dy < self._rect[3]:
            self._hover = True
        else:
            self._hover = False

    def visible(self):
        return self._visible

    def rect(self):
        return self._rect