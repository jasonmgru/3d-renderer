import clickable

class Button(clickable.Clickable):
    def __init__(self, rect, img):
        super().__init__()
        self._rect = rect
        self._img = img
        self._visible = True
        self._type = "button"

    def img(self):
        return self._img