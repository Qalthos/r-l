import tdl

if __name__ == '__main__':
    console = tdl.init(80, 80)

    # Draw the map
    console.drawFrame(0, 0, 80, 80, '#')
    console.drawChar(1, 2, 'J')

    p_x, p_y = 1, 1

    while True:

        console.drawChar(p_x, p_y, '@')

        tdl.flush()

        key = tdl.event.keyWait()
        if key.keychar == 'q':
            break

        elif key.key in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            new_x, new_y = p_x, p_y
            if key.key == 'UP':
                new_y -= 1
            elif key.key == 'LEFT':
                new_x -= 1
            elif key.key == 'DOWN':
                new_y += 1
            elif key.key == 'RIGHT':
                new_x += 1

            print(console.getChar(new_x, new_y)[0])
            if console.getChar(new_x, new_y)[0] == 32:
                console.drawChar(p_x, p_y, ' ')
                p_x, p_y = new_x, new_y
