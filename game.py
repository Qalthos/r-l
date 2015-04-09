from map import Map


game_map = Map()


if __name__ == '__main__':

    while True:
        game_map.repaint()
        if game_map.move_all():
            break
