import importlib
import json

import tdl

import entity


class Window(object):

    entities = []

    def __init__(self):
        self.root = tdl.init(80, 40)

        self._map = tdl.Console(40, 40)
        self.gen_map('floors.json')

        self._text_frame = tdl.Console(40, 40)
        self._text_frame.drawRect(0, 1, 40, 38, '║')
        self._text_frame.drawRect(1, 0, 38, 40, '═')
        self._text_frame.drawChar(0, 0, '╔')
        self._text_frame.drawChar(39, 0, '╗')
        self._text_frame.drawChar(0, 39, '╚')
        self._text_frame.drawChar(39, 39, '╝')

        self._text = tdl.Console(38, 38)
        self._text.setMode('scroll')

    def gen_map(self, filename, floor_number=0):
        self._map.clear()

        with open(filename) as floor_data:
            floor = json.load(floor_data)[floor_number]

        for room in floor['rooms']:
            self._map.drawFrame(room['x'], room['y'], room['w'], room['h'], '#')
        for hall in floor['halls']:
            x, y = hall['x'] - 1, hall['y'] - 1
            if hall['dir'] in 'ns':
                w = 3
                h = hall['len']
                ends = (x + 1, y), (x + 1, y + h - 1)
            elif hall['dir'] in 'ew':
                w = hall['len']
                h = 3
                ends = (x, y + 1), (x + w - 1, y + 1)
            else:
                print("Don't know how to read this hall: {}".format(hall))
            self._map.drawFrame(x, y, w, h, '#')
            for end in ends:
                self._map.drawChar(end[0], end[1], ' ')

        for entity in floor['entities']:
            module, class_ = entity['type'].rsplit('.', 1)
            package = importlib.import_module(module)
            self.entities.append(getattr(package, class_)(entity['x'], entity['y'], self))

    def repaint(self):
        self.root.clear()

        self.root.blit(self._map, width=40)
        self._text_frame.blit(self._text, x=1, y=1, width=38, height=38)
        self.root.blit(self._text_frame, x=40)

        for entity in self.entities:
            entity.draw()

        tdl.flush()

    def move_all(self):
        for entity in self.entities:
            try:
                entity.move()
            except KeyboardInterrupt:
                return True

    def run(self):
        while True:
            self.repaint()
            if self.move_all():
                break

    def check_move(self, x, y):
        if self._map.getChar(x, y)[0] == 35:
            return entity.Wall()

        entities = [e for e in self.entities if e.x == x and e.y == y]
        if entities:
            return entities[0]

        return None

    def print(self, string):
        self._text.printStr(string + '\n')
