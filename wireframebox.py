import clickable

class WireframeBox(clickable.Clickable):
    def __init__(self, wireframe):
        super().__init__()
        self._wireframe = wireframe

    def release(self):
        self._wireframe.set_selected(True)

    def update(self, cursor_pos):
        super().update(cursor_pos)
        min_x, min_y = 100000, 100000
        max_x, max_y = 0, 0
        for n in self._wireframe.nodes():
            if n[0] < min_x:
                min_x = n[0]
            if n[0] > max_x:
                max_x = n[0]
            if n[1] < min_y:
                min_y = n[1]
            if n[1] > max_y:
                max_y = n[1]

        self._rect = (min_x, min_y, max_x-min_x+2, max_y-min_y+2)
            
