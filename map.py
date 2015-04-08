import tdl

class Map(object):

    entities = [(1, 1, '@'), (1, 2, 'J'), ]

    def __init__(self):
        self.console = tdl.init(80, 80)

    def repaint(self):
        self.console.clear()
        self.console.drawFrame(0, 0, 80, 80, '#')

        for entity in self.entities:
            self.console.drawChar(*entity)

        tdl.flush()

    def move_entity(self, index, delta_x, delta_y):
        e = self.entities[index]
        new_x = e[0] + delta_x
        new_y = e[1] + delta_y

        if self.console.getChar(new_x, new_y)[0] == 32:
            self.entities[index] = (new_x, new_y, e[2])
