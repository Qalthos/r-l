import tdl

import entity


class Window(object):

    entities = []

    def __init__(self):
        self.root = tdl.init(80, 40)

        self._map = tdl.Console(40, 40)
        self._map.drawFrame(0, 0, width, height, '#')

        self._text = tdl.Console(38, 38)
        self._text.setMode('scroll')

        self.entities.append(entity.Player(1, 1, '@', self))
        self.entities.append(entity.Walker(1, 2, 'J', self))

    def repaint(self):
        self.root.clear()

        self.root.blit(self._map, width=40)
        self.root.blit(self._text, x=41, y=1)

        for entity in self.entities:
            entity.draw()

        tdl.flush()

    def move_all(self):
        for entity in self.entities:
            try:
                entity.move()
            except NotImplementedError:
                pass
            except KeyboardInterrupt:
                return True

    def run(self):
        while True:
            self.repaint()
            if self.move_all():
                break

    def check_move(self, x, y):
        if not self._map.getChar(x, y)[0] == 32:
            return False
        return not any([e.x == x and e.y == y for e in self.entities])
