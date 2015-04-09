import tdl

import entity


class Map(object):

    entities = []

    def __init__(self):
        self.console = tdl.init(30, 30)
        self.entities.append(entity.Entity(1, 1, '@', self))
        self.entities.append(entity.Walker(1, 2, 'J', self))

    def repaint(self):
        self.console.clear()
        self.console.drawFrame(0, 0, 80, 80, '#')

        for entity in self.entities:
            if hasattr(entity, 'move'):
                entity.move()
            entity.draw()

        tdl.flush()

    def move_entity(self, index, delta_x, delta_y):
        e = self.entities[index]
        new_x = e.x + delta_x
        new_y = e.y + delta_y

        if self.check_move(new_x, new_y):
            e.x = new_x
            e.y = new_y

    def check_move(self, x, y):
        return self.console.getChar(x, y)[0] == 32
