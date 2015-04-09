import tdl

import entity


class Map(object):

    entities = []

    def __init__(self):
        self.console = tdl.init(80, 40)

        # Keep the walls on their own console.
        self._map = tdl.Console(80, 40)
        self._map.drawFrame(0, 0, 80, 40, '#')

        self.entities.append(entity.Player(1, 1, '@', self))
        self.entities.append(entity.Walker(1, 2, 'J', self))

    def repaint(self):
        self.console.clear()
        self.console.blit(self._map)

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

    def check_move(self, x, y):
        if not self._map.getChar(x, y)[0] == 32:
            return False
        return not any([e.x == x and e.y == y for e in self.entities])
