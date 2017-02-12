# -*- encoding: utf8 -*-

import curses


_ = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


I = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
]


V = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
]


O = [
    [1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0]
]


L = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
]


E = [
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
]


G = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
]


def draw_letter(matrix, coords):
    win = curses.newwin(len(matrix), len(matrix) + 1, coords[0], coords[1])
    win.clear()
    win.bkgd(' ', curses.color_pair(1))
    for i in range(len(matrix)):
        win.addstr(i, 0, ''.join('#' if k else ' ' for k in matrix[i]), curses.A_BOLD)
    win.refresh()


def big_heart(stdscr, left_start):
    stdscr.addstr(left_start[0], left_start[1] + 2, '  ', curses.A_REVERSE)
    stdscr.addstr(left_start[0], left_start[1] + 9, '  ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 1, left_start[1] + 1, '    ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 1, left_start[1] + 8, '    ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 2, left_start[1], '      ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 2, left_start[1] + 7, '      ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 3, left_start[1] + 1, '           ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 4, left_start[1] + 2, '         ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 5, left_start[1] + 3, '       ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 6, left_start[1] + 4, '     ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 7, left_start[1] + 5, '   ', curses.A_REVERSE)
    stdscr.addstr(left_start[0] + 8, left_start[1] + 6, ' ', curses.A_REVERSE)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    stdscr.bkgd(' ', curses.color_pair(1))
    height, width = stdscr.getmaxyx()
    heart_size = (8, 13)
    left_start = (height // 2 - heart_size[0] // 2, width // 2 - heart_size[1] // 2)
    # Draw heart
    big_heart(stdscr, left_start)
    stdscr.refresh()
    # Draw letters
    s = [I, _, L, O, V, E, _, O, L, E, G]
    y = 1
    x = 6
    for letter in s:
        draw_letter(letter, (y, x))
        x += 6

    stdscr.getkey()

curses.wrapper(main)
