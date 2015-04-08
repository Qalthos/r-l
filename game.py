import tdl

from map import Map


game_map = Map()


def handle_key(event):
    if event.keychar == 'q':
        return True

    elif event.key in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
        dx, dy = 0, 0
        if event.key == 'UP':
            dy = -1
        elif event.key == 'LEFT':
            dx = -1
        elif event.key == 'DOWN':
            dy = 1
        elif event.key == 'RIGHT':
            dx = 1

        game_map.move_entity(0, dx, dy)


if __name__ == '__main__':

    while True:
        game_map.repaint()
        exit = handle_key(tdl.event.keyWait())
        if exit:
            break
