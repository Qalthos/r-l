import tdl

import entity


class Map(object):

    entities = []

    def __init__(self):
        self.console = tdl.init(30, 30)
        self.entities.append(entity.Player(1, 1, '@', self))
        self.entities.append(entity.Walker(1, 2, 'J', self))

    def repaint(self):
        self.console.clear()
        self.console.drawFrame(0, 0, 80, 80, '#')

        for entity in self.entities:
            try:
                entity.move()
            except NotImplementedError:
                pass
            entity.draw()

        tdl.flush()

    def check_move(self, x, y):
        return self.console.getChar(x, y)[0] == 32
