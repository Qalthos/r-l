import tdl

from entity import Entity, Walker


class Map(object):

    entities = []

    def __init__(self):
        self.console = tdl.init(30, 30)
        self.entities.append(Entity(1, 1, '@', self))
        self.entities.append(Walker(1, 2, 'J', self))

    def repaint(self):
        self.console.clear()
        self.console.drawFrame(0, 0, 80, 80, '#')

        for entity in self.entities:
            if hasattr(entity, 'move'):
                entity.move()
            entity.draw(self.console)

        tdl.flush()

    def move_entity(self, index, delta_x, delta_y):
        e = self.entities[index]
        new_x = e.x + delta_x
        new_y = e.y + delta_y

        if self.console.getChar(new_x, new_y)[0] == 32:
            e.x = new_x
            e.y = new_y
